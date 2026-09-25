import { Controller, Get, Param, Query } from '@nestjs/common';

/**
 * Direct structured-metric endpoints (bypass the agent).
 *   GET /v1/metrics/{year}                     -> raw AnalysisResult (FR01)
 *   GET /v1/metrics/compare?years=..&metric=.. -> year-over-year (FR04)
 * Values are always read verbatim from the DB — never generated (NFR01).
 *
 * SKELETON: placeholders until the data layer is wired in.
 */
@Controller('metrics')
export class MetricsController {
  @Get('compare')
  compare(
    @Query('years') _years: string,
    @Query('metric') _metric: string,
  ): { status: string } {
    return { status: 'not_implemented' };
  }

  @Get(':year')
  byYear(@Param('year') year: string): { year: number; status: string } {
    return { year: Number(year), status: 'not_implemented' };
  }
}
