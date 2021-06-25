import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ConversationsService {

  constructor(private http: HttpClient) {}

  
  getConversations() {
    return this.http.get(environment.apiEndpointServer + '/conversations');
  }

  getConversation(conversation_id: string) {
    return this.http.get(environment.apiEndpointServer + '/conversations/' + conversation_id);
  }

  newConversation(title: string) {
    return this.http.post(environment.apiEndpointServer + '/conversations', {'title': title});
  }

  searchConversations(search_text: string) {
    return this.http.post(environment.apiEndpointServer + '/conversations/search', {'search_text': search_text});
  }
}
