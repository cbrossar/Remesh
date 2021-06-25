import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ConversationsService } from './conversations.service';

describe('ConversationsService', () => {

  beforeEach(() => TestBed.configureTestingModule({
    imports: [HttpClientTestingModule], 
    providers: [ConversationsService]
  }));

  it('should be created', () => {
    const service: ConversationsService = TestBed.get(ConversationsService);
    expect(service).toBeTruthy();
  });
});
