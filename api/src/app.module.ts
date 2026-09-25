import { Module } from '@nestjs/common';
import { HealthController } from './health/health.controller';
import { QueryController } from './modules/query/query.controller';
import { MetricsController } from './modules/metrics/metrics.controller';
import { OrchestrationClient } from './common/orchestration.client';

/**
 * Root module. API layer only — no AI logic here (see docs/03-architecture.md).
 * Controllers translate the public HTTP contract into calls to the Agent
 * Orchestration layer via {@link OrchestrationClient}.
 */
@Module({
  controllers: [HealthController, QueryController, MetricsController],
  providers: [OrchestrationClient],
})
export class AppModule {}
