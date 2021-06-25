import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ThoughtService } from './thought.service';

describe('ThoughtService', () => {
  beforeEach(() => TestBed.configureTestingModule({
    imports: [HttpClientTestingModule], 
    providers: [ThoughtService]
  }));

  it('should be created', () => {
    const service: ThoughtService = TestBed.get(ThoughtService);
    expect(service).toBeTruthy();
  });
});
