import { Component, OnInit } from '@angular/core';
import { ConversationsService } from '../../services/conversations.service'
import {MatDialog, MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import { DialogComponent } from '../dialog/dialog.component';

export interface Conversation {
  title: string;
}

@Component({
  selector: 'app-conversations',
  templateUrl: './conversations.component.html',
  styleUrls: ['./conversations.component.css']
})
export class ConversationsComponent implements OnInit {

  constructor(private conversationsService: ConversationsService, public dialog: MatDialog) { }

  conversations: Conversation[] = [];
  label: string = '';
  title: string = '';
  question: string = '';
  search_term: string = '';

  ngOnInit(): void {
    this.getConversations();
  }

  openDialog(type:string): void {

    if(type == 'NEW') {
      this.question = 'What is the title of your new conversation?'
      this.label = 'Title'
    } else {
      this.label = 'Search Term'
      this.question = 'What would you like to search for?'
    }

    const dialogRef = this.dialog.open(DialogComponent, {
      width: '250px',
      data: {label: this.label, text: this.title, question: this.question}
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      if(type == 'NEW') {
        this.title = result;
        if(this.title) {
          this.conversationsService.newConversation(this.title).subscribe( data => {
            this.getConversations();
          });
        }
        this.title = '';
      } else{
        this.search_term = result;
        if(this.search_term) {
          this.conversationsService.searchConversations(this.search_term).subscribe( data => {
            console.log(data);
            this.conversations = data as any[];
          });
        }
        this.title = '';
      }
      
    });
  }

  getConversations() {
    this.conversationsService.getConversations().subscribe( data => {
      console.log(data);
      this.conversations = data as any[];
    }, error => {
      console.log(error);
    });
  }

}
