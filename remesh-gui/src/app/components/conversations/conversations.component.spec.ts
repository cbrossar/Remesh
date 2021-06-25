import { ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ConversationsComponent } from './conversations.component';
import { ConversationsService } from 'src/app/services/conversations.service';
import { DialogComponent } from '../dialog/dialog.component';
import { MatDialog } from '@angular/material/dialog';


describe('ConversationsComponent', () => {
  let component: ConversationsComponent;
  let fixture: ComponentFixture<ConversationsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [HttpClientTestingModule, MatDialog], 
      providers: [ConversationsService],
      declarations: [ConversationsComponent, DialogComponent]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConversationsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
