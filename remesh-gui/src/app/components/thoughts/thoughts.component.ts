import { Component, OnInit } from '@angular/core';
import { MessagesService } from 'src/app/services/messages.service';
import { ActivatedRoute } from '@angular/router';
import { DialogComponent } from '../dialog/dialog.component';
import { ThoughtService } from 'src/app/services/thought.service';
import { MatDialog } from '@angular/material/dialog';

export interface Thought {
  text: string;
}

@Component({
  selector: 'app-thoughts',
  templateUrl: './thoughts.component.html',
  styleUrls: ['./thoughts.component.css']
})
export class ThoughtsComponent implements OnInit {

  message_id: any = '';
  message_text: string = '';
  thoughts: Thought[] = [];

  question: string = '';
  label: string = '';
  thought: string = '';

  constructor(private messagesService: MessagesService, public route: ActivatedRoute, private thoughtService: ThoughtService, 
    public dialog: MatDialog) { }

  ngOnInit(): void {
    this.message_id = this.route.snapshot.paramMap.get('id');
    this.getMessage();
  }

  getMessage() {
    this.messagesService.getMessage(this.message_id).subscribe( data => {
      console.log(data);
      var d = data as any;
      this.message_text = d['text'];
      this.thoughts = d['thoughts'];
      console.log(this.thoughts);

    }, error => {
      console.log(error);
    });
  }

  openDialog(): void {

    this.question = 'What message would you like to add to the conversation?'
    this.label = 'Message'

    const dialogRef = this.dialog.open(DialogComponent, {
      width: '250px',
      data: {label: this.label, text: '', question: this.question}
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
        this.thought = result.text;
        if(this.thought) {
          this.thoughtService.newThought(this.message_id, this.thought).subscribe( data => {
            console.log(data);
            this.getMessage();
          });
          this.thought = '';
        }
      
    });
  }

}
