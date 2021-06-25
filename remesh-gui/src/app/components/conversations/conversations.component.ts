import { Component, OnInit } from '@angular/core';
import { ConversationsService } from '../../services/conversations.service'
import { MatDialog } from '@angular/material/dialog';
import { DialogComponent } from '../dialog/dialog.component';
import { Router } from '@angular/router'

export interface Conversation {
  title: string;
}

@Component({
  selector: 'app-conversations',
  templateUrl: './conversations.component.html',
  styleUrls: ['./conversations.component.css']
})
export class ConversationsComponent implements OnInit {

  constructor(private conversationsService: ConversationsService, public dialog: MatDialog, private router: Router) { }

  conversations: Conversation[] = [];
  label: string = '';
  title: string = '';
  question: string = '';
  search_text: string = '';

  ngOnInit(): void {
    this.getConversations();
  }

  getConversations() {
    this.conversationsService.getConversations().subscribe( data => {
      console.log(data);
      this.conversations = data as any[];
    }, error => {
      console.log(error);
    });
  }

  goToConversation(conversation: any) {
    console.log(conversation);
    this.router.navigate(['conversations', conversation.id, 'messages']);
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
      width: '300px',
      data: {label: this.label, text: '', question: this.question}
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      if(type == 'NEW') {
        this.title = result.text;
        if(this.title && result.date) {
          console.log('herro');
          this.conversationsService.newConversationDate(this.title, result.date).subscribe( data => {
            this.getConversations();
          });
        }
        else if(this.title) {
          this.conversationsService.newConversation(this.title).subscribe( data => {
            this.getConversations();
          });
        }
        this.title = '';
      } else{
        this.search_text = result.text;
        if(this.search_text) {
          this.conversationsService.searchConversations(this.search_text).subscribe( data => {
            console.log(data);
            this.conversations = data as any[];
          });
        }
        this.search_text = '';
      }
      
    });
  }

}
