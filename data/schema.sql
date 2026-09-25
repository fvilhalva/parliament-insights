-- Parliament Insights — operational schema (see docs/04-data-model.md).
-- A read-only projection of the thesis artifacts + fields generated at this
-- layer (embedding, community summaries). NFR10: source artifacts are never
-- mutated; AnalysisResult is append-only.

CREATE EXTENSION IF NOT EXISTS vector;      -- pgvector
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Imported from the thesis metrics CSV.
CREATE TABLE IF NOT EXISTS deputy (
    deputy_id   INTEGER PRIMARY KEY,        -- natural key from Chamber data
    name        VARCHAR(255) NOT NULL,
    party_code  VARCHAR(10),
    state_code  CHAR(2)
);

-- Imported + enriched. `embedding` is generated at this layer (384-d).
CREATE TABLE IF NOT EXISTS proposition (
    proposition_id INTEGER PRIMARY KEY,
    type           VARCHAR(5),
    year           INTEGER NOT NULL,
    summary_text   TEXT,
    embedding      vector(384)
);

-- Normalized replica of the co-authorship graph edges (from GEXF).
CREATE TABLE IF NOT EXISTS coauthorship_edge (
    edge_id      UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    deputy_id_a  INTEGER NOT NULL REFERENCES deputy(deputy_id),
    deputy_id_b  INTEGER NOT NULL REFERENCES deputy(deputy_id),
    weight       REAL,
    year         INTEGER NOT NULL
);

-- Louvain / Label Propagation assignment per deputy/year (from metrics CSV).
CREATE TABLE IF NOT EXISTS community_assignment (
    assignment_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    deputy_id     INTEGER NOT NULL REFERENCES deputy(deputy_id),
    year          INTEGER NOT NULL,
    community_id  INTEGER NOT NULL,
    method        VARCHAR(20)
);

-- Imported from analysis_{year}.json. Append-only; keyed by year (NFR10).
CREATE TABLE IF NOT EXISTS analysis_result (
    year               INTEGER PRIMARY KEY,
    n_nodes            INTEGER,
    n_edges            INTEGER,
    density            REAL,
    modularity_louvain REAL,
    p_value            REAL,
    raw_json           JSONB
);

-- Generated at this layer: LLM-result cache (FR07). Includes model_used (NFR05).
CREATE TABLE IF NOT EXISTS community_summary (
    summary_id     UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    year           INTEGER NOT NULL REFERENCES analysis_result(year),
    community_id   INTEGER NOT NULL,
    generated_text TEXT NOT NULL,
    model_used     VARCHAR(100),
    created_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (year, community_id)
);

-- Vector index for similarity search (FR02). Tune lists after data load.
CREATE INDEX IF NOT EXISTS idx_proposition_embedding
    ON proposition USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);

CREATE INDEX IF NOT EXISTS idx_proposition_year ON proposition (year);
CREATE INDEX IF NOT EXISTS idx_assignment_year_community
    ON community_assignment (year, community_id);
