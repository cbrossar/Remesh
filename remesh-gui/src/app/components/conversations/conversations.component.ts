import { Component, OnInit } from '@angular/core';
import { ConversationsService } from '../../services/conversations.service'

export interface Conversation {
  title: string;
}

@Component({
  selector: 'app-conversations',
  templateUrl: './conversations.component.html',
  styleUrls: ['./conversations.component.css']
})
export class ConversationsComponent implements OnInit {

  constructor(private conversationsService: ConversationsService) { }

  conversations: Conversation[] = []

  ngOnInit(): void {
    this.conversationsService.getConversations().subscribe( data => {
      console.log(data);
      this.conversations = data as any[];
      console.log(this.conversations)
    },
    (error) => {
      console.log(error);
    })
  }

}
