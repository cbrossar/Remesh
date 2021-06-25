import { Component, OnInit } from '@angular/core';
import { ConversationsService } from 'src/app/services/conversations.service';
import { Router, ActivatedRoute } from '@angular/router';
import { DialogComponent } from '../dialog/dialog.component';
import { MatDialog } from '@angular/material/dialog';
import { MessagesService } from 'src/app/services/messages.service';

export interface Message {
  text: string;
}

@Component({
  selector: 'app-messages',
  templateUrl: './messages.component.html',
  styleUrls: ['./messages.component.css']
})
export class MessagesComponent implements OnInit {
  conversation_id: any = '';
  conversation_title: string = '';
  messages: Message[] = [];

  question: string = '';
  label: string = '';
  message: string = '';
  search_text: string = '';


  constructor(private conversationsService: ConversationsService, private route: ActivatedRoute,
     public dialog: MatDialog, private router: Router, private messageService: MessagesService) { 
  }


  ngOnInit(): void {
    this.conversation_id = this.route.snapshot.paramMap.get('id');
    this.getConversation();
  }

  getConversation() {
    this.conversationsService.getConversation(this.conversation_id).subscribe( data => {
      console.log(data);
      var d = data as any;
      this.conversation_title = d['title'];
      this.messages = d['messages'];
      console.log(this.messages);

    }, error => {
      console.log(error);
    });
  }

  goToMessage(message: any) {
    console.log('herro');
    console.log(message);
    this.router.navigate(['messages', message.id, 'thoughts']);
  }


  openDialog(type:string): void {

    if(type == 'NEW') {
      this.question = 'What message would you like to add to the conversation?'
      this.label = 'Message'
    } else {
      this.label = 'Search Term'
      this.question = 'What would you like to search for?'
    }

    const dialogRef = this.dialog.open(DialogComponent, {
      width: '250px',
      data: {label: this.label, text: '', question: this.question}
    });

    dialogRef.afterClosed().subscribe(result => {
      console.log('The dialog was closed');
      if(type == 'NEW') {
        this.message = result;
        if(this.message) {
          this.messageService.newMessage(this.conversation_id, this.message).subscribe( data => {
            console.log(data)
            this.getConversation();
          });
          this.message = '';
        }
      } else{
        this.search_text = result;
        if(this.search_text) {
          this.messageService.searchMessages(this.conversation_id, this.search_text).subscribe( data => {
            console.log(data);
            this.messages = data as any[];
          });
        }
      }
      
    });
  }

}
