import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MessagingSystemComponent } from './messaging-system.component';

describe('MessagingSystemComponent', () => {
  let component: MessagingSystemComponent;
  let fixture: ComponentFixture<MessagingSystemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MessagingSystemComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MessagingSystemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
