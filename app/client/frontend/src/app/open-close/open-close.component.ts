import { Component } from '@angular/core';

@Component({
  selector: 'app-open-close',
  templateUrl: './open-close.component.html',
  styleUrls: ['./open-close.component.scss'],
})
export class OpenCloseComponent {
  show = false;
  startBracket = '{';
  endBracket = '}';
  codeValue = `\`
    <h1> {{message}} </h1> 
  \``;

  space = '...';
}
