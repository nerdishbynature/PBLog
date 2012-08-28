//
//  PBLogExampleViewController.h
//  PBLogExample
//
//  Created by Piet Brauer on 28.08.12.
//  Copyright (c) 2012 Piet Brauer. All rights reserved.
//

#import <UIKit/UIKit.h>
#import "PBLog.h"

@interface PBLogExampleViewController : UIViewController <UITextFieldDelegate, NSURLConnectionDelegate>{
    IBOutlet UITextField *textField;
    IBOutlet UIButton *sendButton;
}

@property (nonatomic, retain) UITextField *textField;
@property (nonatomic, retain) UIButton *sendButton;

-(IBAction)sendMessage:(id)sender;

@end
