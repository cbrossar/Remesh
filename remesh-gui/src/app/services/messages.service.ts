import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class MessagesService {

  constructor(private http: HttpClient) { }

  getMessage(message_id: string) {
    return this.http.get(environment.apiEndpointServer + '/messages/' + message_id);
  }

  newMessage(conversation_id: number, text: string) {
    return this.http.post(environment.apiEndpointServer + '/messages', {'conversation': conversation_id, 'text': text});
  }

  searchMessages(conversation_id: number, search_text: string) {
    return this.http.post(environment.apiEndpointServer + '/messages/search', {'conversation': conversation_id, 'search_text': search_text});
  }
}
