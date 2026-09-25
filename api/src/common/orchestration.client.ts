import { Injectable } from '@nestjs/common';

/**
 * The single Node -> Python boundary (docs/03-architecture.md, NFR07).
 * Forwards a classified request to the Agent Orchestration layer.
 *
 * SKELETON: not yet wired to the real agent service.
 */
@Injectable()
export class OrchestrationClient {
  private readonly baseUrl = process.env.AGENT_BASE_URL ?? 'http://agent:8000';

  async invoke(_question: string, _context?: Record<string, unknown>): Promise<never> {
    throw new Error(
      `OrchestrationClient.invoke() not implemented — will POST to ${this.baseUrl}/invoke`,
    );
  }
}
