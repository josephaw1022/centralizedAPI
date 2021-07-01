import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';
import * as $ from 'jquery';
@Component({
  selector: 'app-open-close',
  templateUrl: './open-close.component.html',
  styleUrls: ['./open-close.component.scss'],
})
export class OpenCloseComponent implements OnInit {
  startBracket = '{';
  endBracket = '}';
  codeValue = `\`<h1> {{message}} </h1>\` `;

  space = '...';

  showCircle = false;

  ngOnInit() {}
}
