import { Body, Controller, Post } from '@nestjs/common';

interface QueryRequest {
  question: string;
  context?: { preferred_language?: string };
}

/**
 * POST /v1/query — single agent entry point (FR05). Routes to FR01/FR02/FR03
 * by classified intent. See docs/05-api-design.md.
 *
 * SKELETON: returns 501-style placeholder until the agent is wired in.
 */
@Controller('query')
export class QueryController {
  @Post()
  query(@Body() _body: QueryRequest): { intent: string; status: string } {
    return { intent: 'unrouted', status: 'not_implemented' };
  }
}
