# Seq2seq chatbot with attention mechanism

This is a implementation of seq2seq chatbot with attention.

## Introduction

Basically, there are three kinds of chatbot, task-oriented chatbot, chitchat chatbot and retrieval based chatbot. My previous work focus on 
task-oriented chatbot. Because in LARC, we have meet-up data and we want to build a chatbot to recommend evevnts in Singapore according to 
user requirement that the system get during conversation. This kind of model is very difficult to train in an end-to-end fashion. 
Retrieval based chatbot is relatively simple, the main difference of various approches is how to calculate similarity score. 
Here I don't want to talk much on that. The final category of chatbot, the one for chitchat is more interesting. 
It is built on top of the seq2seq framework, it is a data driven method and can be trained end-to-end. This project focuses on seq2seq model. 
I followed the Pytorch Seq2seq tutorial and made some modifications based on the current senario and dataset.
 

## Methodology

1. Prepare data for for the encoder (OpenSubtitle Dataset and Twitter Triplet Dataset)
2. Build a encoder model and a decoder model with attention
3. Train the model and visualize attention 
4. Calculate BLEU score and perplexity
5. Use the model to converse with people

## Result
1. lool i broke three of my mums so i ve been banned from doing it lol </br>
Truth: antonyy i ve totally broke it hahah hard times </br>
Generated: antonyy i ve totally broke it hahah hard times </br>

2. cus i told her your very protective of me </br>
Truth: breon lol why i m not mean </br>
Generated: breon lol why i m not mean </br>

3. itslauren remember that one day you forced him to eat golden grahms yea that day </br>
Truth: kid uhmmm when did he tell you this </br>
Generated: kid did when you did he have to get this morning </br>

4. not to sure just fill the form in anyways don t think we need t pay today </br>
Truth: forms have to be given to paul today </br>
Generated: forms have to be given to paul today </br>

## References:
https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html </br>
http://www.kdd.org/exploration_files/19-2-Article3.pdf </br>
