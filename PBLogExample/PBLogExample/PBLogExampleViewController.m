//
//  PBLogExampleViewController.m
//  PBLogExample
//
//  Created by Piet Brauer on 28.08.12.
//  Copyright (c) 2012 Piet Brauer. All rights reserved.
//

#import "PBLogExampleViewController.h"

@implementation PBLogExampleViewController
@synthesize sendButton;
@synthesize textField;

- (id)initWithNibName:(NSString *)nibNameOrNil bundle:(NSBundle *)nibBundleOrNil
{
    self = [super initWithNibName:nibNameOrNil bundle:nibBundleOrNil];
    if (self) {
        // Custom initialization
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    // Do any additional setup after loading the view from its nib.
    [self.textField becomeFirstResponder];
}

- (void)viewDidUnload
{
    [super viewDidUnload];
    // Release any retained subviews of the main view.
    // e.g. self.myOutlet = nil;
}

- (BOOL)shouldAutorotateToInterfaceOrientation:(UIInterfaceOrientation)interfaceOrientation
{
    return (interfaceOrientation == UIInterfaceOrientationPortrait);
}

-(void)sendMessage:(id)sender{
    PBLog(@"%@",self.textField.text);
    [self.textField setText:@""];
}

-(BOOL)textFieldShouldReturn:(UITextField *)textField{
    [self sendMessage:nil];
    return YES;
}

-(void)dealloc{
    self.sendButton = nil;
    self.textField = nil;
    
    [sendButton release];
    [textField release];
    [super dealloc];
}

@end
