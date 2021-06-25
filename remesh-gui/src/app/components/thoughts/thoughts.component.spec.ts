import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { MessagesService } from 'src/app/services/messages.service';
import { ThoughtService } from 'src/app/services/thought.service';
import { ThoughtsComponent } from './thoughts.component';

describe('ThoughtsComponent', () => {
  let component: ThoughtsComponent;
  let fixture: ComponentFixture<ThoughtsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HttpClientTestingModule], 
      providers: [MessagesService, ThoughtService],
      declarations: [ThoughtsComponent]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ThoughtsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
