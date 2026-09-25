import { HealthController } from '../src/health/health.controller';
import { MetricsController } from '../src/modules/metrics/metrics.controller';

describe('skeleton controllers', () => {
  it('health check reports ok', () => {
    expect(new HealthController().check()).toEqual({
      status: 'ok',
      service: 'parliament-insights-api',
    });
  });

  it('metrics byYear echoes a numeric year (placeholder)', () => {
    const res = new MetricsController().byYear('2024');
    expect(res.year).toBe(2024);
    expect(res.status).toBe('not_implemented');
  });
});
