#include <iostream>
using namespace std;

struct Node{
  int data;
  Node* next=NULL;
  Node* prev=NULL;
};

class list{
  Node* head=NULL;
public:
  void insert(int data){
    Node* node= new Node;
    node->data=data;
    if(head==NULL){
      head=node;
    }else{
      Node* n=head;
      while(n->next!=NULL){
        n=n->next;
      }
      n->next=node;
      node->prev=n;
    }
  }
  void show(){
    Node* n= head;
    while (n->next!=NULL) {
      cout<<n->data<<" ";
      n=n->next;
    }
    cout<<n->data<<endl;
  }
};

int main(){
  list x;
  for(int i=0;i<10;i++){
    x.insert(i+1);
  }
  x.show();

}
