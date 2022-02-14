# An Interface for Bi-directional Icon-Based Communication

### David Kang

A project proposal submitted in partial fulfillment of the requirements of the degree of: Master of Science in Computer Science & Software Engineering

University of Washington

## Overview:

This project will aim to offer further accessibility to individuals who rely on icon-based
communication (IBC). Through identification of user-specified icons and their linkages
to user-defined meanings, this project will bridge the communication gap that typically
exists for IBC users when interacting with the systems of the modern world. The project
application will be bi-directional, allowing users to convert icons into text, while also
converting text-based language into any applicable icons.

## Background:

Augmentative and Alternative Communication (AAC) is a broad scale categorization of
different means or mechanisms of communication that are used to supplement, or
compensate for, impairments in normal speech language production [5]. Augmentative
communication is any form of AAC which is used to supplement existing speech.
Alternative communication refers to forms of AAC that replace typical speech [1]. At its
highest level, AAC can be considered any form of communication which is not directly
related to speech. Things such as facial expressions, gestures, or drawings can be
considered as AAC. More commonly, AAC is viewed through a clinical lens, specifically
relating to individuals who suffer from communication disorders [4]. In these cases,
AAC refers to techniques or strategies used to maximize an individual’s ability to
communicate. AAC systems may be temporary, or permanent [1,5].

Icon-based communication (IBC), or symbol-based communication, is a subset of
Alternative AAC strategies. IBC is typically intended for individuals who are unable to
communicate using speech or text [6]. This could be due to lack of literacy skills,
cognitive disorders, or physical disorders. In lieu of these classic means of
communication, IBC users will instead communicate via symbols. Most often, these are
standardized symbols that are found in many different forms of media. These symbols
will carry an inherent meaning that is understood in many different cultures [1,6].

IBC has some inherent advantages over speech or text-based communication.
Primarily, icons and symbols carry much more meaning than an average word and can
change meaning depending on context. However, there are also some unavoidable
flaws, the most obvious being the limited scope of symbols [2]. IBC users most often use
the strategy to communicate with individuals who would otherwise use speech or text.
As a result, the symbols chosen in most IBC strategies must be somewhat universal and
understood by others across cultural boundaries [1,7].


## Project Vision:

### Problem

```
Accessibility for IBC users is a growing field, but nevertheless incomplete. The
majority of systems that exist to aid IBC users focus on allowing them to
communicate with traditional speakers [10,11]. These tools have been effective in
allowing icons to be translated into text or voice, but they fail to aid IBC users who
have difficult parsing written text. The need exists for a tool which can effectively
offer bi-directional communication between icon and text-based communication
[13,14].

This need is exacerbated by the growing dependence on the web for all parts of life.
Many interactions that would previously have been carried out in-person have
transitioned to being web based, and thus tend to rely on text-based
communication [14].
```
### Goals

```
At a high level, the purpose of this project is to create the backbone for a system
which may aid individuals who use IBC in their day-to-day life. More specifically,
the intent is to aid IBC users in consuming content designed for traditional
communicators, while also offering a means to communicate themselves. The ideal
end result would be capable of performing the necessary functions to facilitate
communication from a text-based medium to IBC and vis-versa.
```
### Audience

```
The beneficiaries of this project will be IBC users, though they likely will not
represent the target audience. It is unlikely that this project results in a fully
functional application that is ready for end-users. Instead, the audience for this
project would be developers who would be interested in building front-end
applications which could utilize this project’s system. With this in mind, the focus
of this project will be refining the mechanisms for IBC-to-text translation and all
front-end work will be considered ancillary.
```

## Criteria:

| Level of Success | Functionality                                                          |
|:----------------:|------------------------------------------------------------------------|
| Minimum          |- Correlate pre-defined icons with user-defined meanings                |
|                  |- Recognize exact user-defined meanings within a text string            |
|                  |- Report detected meanings to the user through icons                    |
| Expected         |- Allow users to upload known icons and associate them with meanings    |
|                  |- Provide a means to create text strings using icons alone              |
|                  |- Include audio capability to read out icon names or text strings       |
|                  |- Allow users to convert given text into associated icons               |
| Aspirational     |- Parse text from an image and associate it with user-defined meanings  |
|                  |- Allow users to correlate meanings to personalized digital icons       |
|                  |- Recognize hand-drawn icons                                            |
|                  |- Include voice-to-text translation capable of converting verbal input into to text before associating it with a known symbol                                           |
|                  |- Understand text strings that contain similar, but not exact, meanings to known icons                                                                                 |
|                  |- Perform icon detection and recognition on videos                      |



### Definition of quality

```
Measuring the quality of this project will be an inherently subjective task. This
project would be deemed to be successful if it is able to adequately translate
between text strings and icons. Determining what constitutes “adequate” will
depend on the user experience when using the system. A well-produced system
will create translations that are understandable without tedious amounts of effort.

The primary metric that will be used for measuring this project’s success will be
translation accuracy. For the purposes of this project, translation accuracy will be
defined as the percentage of correct translations created when moving from IBC to
text and vis-versa. This metric will likely require manual checking of test cases to
create “correct” baseline translations.

The specific value which defines success will need to be calibrated based on user
experience. The target value should represent a point at which the translations
created by the system are intelligible, but require minimal effort to understand.
Values above this mark will indicate increasing levels of success.
```

## What tools exist?

Current options for users of IBC primarily focus on producing text from an icon-based
input. These tools almost all utilize some form of visual or tactile aid for users to enter
an input in the form of an icon or symbol [3,13]. Some examples of existing tools are:

|SymbolStix||
|:-|-|
|A collection of different tools which include pictures alongside a text definition or meaning. These tools focus on allowing users to learn text-based language through an iconographical means [8].|<img src="https://raw.githubusercontent.com/DaviidK/ibc-translator/main/Documentation/Images/SymbolStix.png" width=1000px/>|

|Boardmaker||
|:-|-|
|A software solution focused on allowing IBC users to communicate with traditional speakers. This product uses pre-defined sets of icons to give meaning to symbols. Users are given the option to select from different sets or create their own board using a combination of icons from different sets [12]|<img src="https://raw.githubusercontent.com/DaviidK/ibc-translator/main/Documentation/Images/Boardmaker.jpg" width=800px/>|


|PECS||
|:-|-|
|The Picture Exchange Communication System is another solution which aims to teach text-based communication gradually using increasingly complex pictures. The system begins with basic symbols and meanings before progressing slowly towards sentence structure and conversation [9].|<img src="https://raw.githubusercontent.com/DaviidK/ibc-translator/main/Documentation/Images/PECS.jpg" width=700px/>|

## Value proposition:
The list of tools presented above is not comprehensive, but it does represent the functionality of options available to IBC users today. These tools by and large focus on moving from an icon or symbol to text, but few options exist to translate in the other direction [10,11,13]. This project will aim to provide new functionality to bridge this gap, and allow users to understand information that they may normally struggle to comprehend.


## Resources and Constraints:
The following functionalities will be sourced from existing methods:
```
- Object detection
- Text recognition
- Text-to-speech
```
The exact libraries to be used will be determined during the beginning stages of this project, and will be chosen based on accuracy, ease of integration, and ease-of-use from a user’s perspective.

By using third-party libraries, this project will be inherently constrained by the functionalities given in these libraries. A large of effort will be allocated into optimizing these technologies as much as possible for this application, but any underlying flaws in each library may carry over to this project’s system.

## References
```
[1] American Speech-Language Hearing Association. Augmentative and Alternative Communication
(AAC).
https://www.asha.org/public/speech/disorders/AAc/

[2] Shiran Dudy and Steven Bedrick. 2019. Compositional Language Modeling for Icon-Based
Augmentative and Alternative Communication. Cent. Spoke Lang. Underst. (2019), 25–32.
DOI:https://doi.org/10.18653/v1/w18-3404

[3] Enabling Devices. Communicators - AAC Devices.
https://enablingdevices.com/product-category/communication-devices/

[4] Rachel Hopf. 2016. The Augmentative/Alternative Communication Spectrum. Indiana University
Bloomington. 
https://www.iidc.indiana.edu/irca/articles/the-augmentative-alternative-communication-spectrum.html

[5] Hypoxic-Ischemic Encephalopathy Help Center. Augmentative and Alternative Communication.
https://hiehelpcenter.org/treatment/speech-language-pathology/augmentative-alternative-communications-systems-aacs/

[6] Literacy for All. Symbol-Based Communication.
https://literacyforallinstruction.ca/symbol-based-communication/

[7] Lumen Learning. Symbols and Culture.
https://courses.lumenlearning.com/culturalanthropology/chapter/symbols-and-culture/

[8] n2y. SymbolStix.
https://www.n2y.com/symbolstix-prime/

[9] National Autism Resources. The Picture Exchange Communication System (PECS).
https://nationalautismresources.com/the-picture-exchange-communication-system-pecs/

[10] National Institute of Health. Assistive Devices for People with Hearing, Voice, Speech, or Language Disorders.
https://www.nidcd.nih.gov/health/assistive-devices-people-hearing-voice-speech-or-language-disorders

[11] Tzvi Schectman. 7 Assistive Communication Apps in the iPad App Store. FriendshipCircle
https://www.friendshipcircle.org/blog/2011/02/07/7-assistive-communication-apps-in-the-ipad-app-store/

[12] Tobii Dynavox LLC. Boardmaker.
https://goboardmaker.com/

[13] Holly Tuke. 2021. Assistive technology devices: How disabled people use the web. Big Hack.
https://bighack.org/assistive-technology-devices-definitions-how-disabled-people-use-the-web/

[14] Karl Wiegand. 2014. Intelligent assistive communication and the web as a social medium. W4A 2014 - 11th Web All Conf. (2014), 3–4. 
DOI:https://doi.org/10.1145/2596695.
```