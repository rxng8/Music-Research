# X-Sig collection of ideas and literature search:

## Our idea and interests:
* Interative audio (or midi) generator based on the current state of event (game, program, etc.)
* Interative audio (or midi) generator based on human action captured in image or video.
* Personality from speech

## Roblox problems of interest:
* moderation for audio (bullying, rage, copyright moderation)
* good music in games (royalty free)
* sentiment analysis of user experience for developers, can be any sensory input.
* VR support being revived and would allow guesture detection
* better accessibility support for visual problems, so audio only game: The Vale - Shadow of the Crown
* add sound effects according to speech recognition/text
* audio search (user describes or imitates sound and finds an appropriate sound resource)

## Official Challenge:
* Website for the chahllenge: https://www.yetanotherfreedman.com/resources/challenge_haaisam.html

# Ideas Analysis and Initial Literature Search (Ranking from first preference (top item) to last preference (bottom item))

## 1. Sentiment Recognition of speech in Roblox players' conversation. This is `[Music Sentiment Analysis task]`
1. Potential dataset/benchmark: IEMOCAP
2. Potential architecture: 
   * Fusion of CNN and existed ASR model?
3. Potential expansion: 
   * Experiemnt with operation in the fusion model?
4. Resources:
   * [https://www.researchgate.net/publication/311990861_Real-Time_Speech_Emotion_and_Sentiment_Recognition_for_Interactive_Dialogue_Systems](https://www.researchgate.net/publication/311990861_Real-Time_Speech_Emotion_and_Sentiment_Recognition_for_Interactive_Dialogue_Systems): They use cnn to detect categorical emotion
       * Dataset they use: https://www.openslr.org/51/
       * Label: commercial API. 6 categorical classes.
       * Architecture: SVM, CNN
    * [https://www.degruyter.com/document/doi/10.1515/jisys-2022-0001/html](https://www.degruyter.com/document/doi/10.1515/jisys-2022-0001/html): Deep learning intuition of speech sentiment analysis.
    * [https://arxiv.org/abs/2112.06603](https://arxiv.org/abs/2112.06603): This paper is really good! It has two separate network for semantic text and sound, then fuse them toghether by Add operation.
    * [https://arxiv.org/abs/1911.09762](https://arxiv.org/abs/1911.09762): This paper utilize the existed ASR (Automatic Speech Recognition) model to train the decoder of sentiment
       * Benchmark:
          * IEMOCAP database
          * SWBD-sentiment database
   * [https://aclanthology.org/2020.lrec-1.806/](https://aclanthology.org/2020.lrec-1.806/): This is A Large Scale Speech Sentiment Corpus

## 2. Interative audio (or midi) generator based on the current state of event (game, program, etc.) E.g Game pig. This is the `[Automatic Music Generation with Features task]`
1. Potential infrastructure:
   * First, we manually label the desired emotion of each state of the game (the emotion labelling scheme corresponds to the labeling scheme of the music corpus).
   * Second, we have to integrate the emotion feature of music to the input of the music generator, toghether with the actual music input. The output will be the same piece of music but move forward a step.
   * A step forward is to merge the state of the game (feature of vector) to the music generator input
2. Midi file Structure:
   * Overall Structure: http://www.ccarh.org/courses/253/handout/smf/
   * Detailed Structure: http://www.music.mcgill.ca/~ich/classes/mumt306/StandardMIDIfileformat.html
3. Technical Midi Processing with Mido:
   * Mido docs: https://mido.readthedocs.io/en/latest/index.html
   * Mido Tutorial: https://www.twilio.com/blog/working-with-midi-data-in-python-using-mido
4. Sound font for playing midi file (and demo midi file): http://www.schristiancollins.com/generaluser.php
5. Techincal sound generation with tensorflow: 
   * https://www.tensorflow.org/tutorials/audio/music_generation
   * https://magenta.tensorflow.org/gansynth
   * [https://towardsdatascience.com/generating-music-using-deep-learning-cb5843a9d55e](https://towardsdatascience.com/generating-music-using-deep-learning-cb5843a9d55e): A fun practice
6. Resources:
   * [https://arxiv.org/abs/2105.09046](https://arxiv.org/abs/2105.09046): This paper talks about using LSTMNN in music generation
   * [https://paperswithcode.com/task/music-generation](https://paperswithcode.com/task/music-generation): The collection of state-of-the-art papers, code, database, and benchmarks regarding the field AMG (Automatic Music Generation)
   * [https://paperswithcode.com/paper/deep-learning-techniques-for-music-generation](https://paperswithcode.com/paper/deep-learning-techniques-for-music-generation): A literature review of different ways of using deep learning (deep artificial neural networks) to generate musical content. The code of this paper is [https://github.com/napulen/MiniBach](https://github.com/napulen/MiniBach)
   * [https://www.catalyzex.com/s/music%20generation](https://www.catalyzex.com/s/music%20generation): Collection of music generation resources (Paper/model/code).
   * [https://github.com/umbrellabeach/music-generation-with-DL](https://github.com/umbrellabeach/music-generation-with-DL): Another collection of music generation resources.

## 3. Interative audio (or midi) generator based on human action captured in image or video:
* This is a fusion of `[Action Recognition task]` and `[Automatic Music Generation with Features task]`

## 4. Audio search (user describes or imitates sound and finds an appropriate sound resource) - `[The humming problem]`
* [https://scholarworks.sjsu.edu/cgi/viewcontent.cgi?article=1895&context=etd_projects](https://scholarworks.sjsu.edu/cgi/viewcontent.cgi?article=1895&context=etd_projects): This document is very helpful in gaining insight into the problem.
* [https://www.cs.cornell.edu/zeno/papers/humming/humming.pdf](https://www.cs.cornell.edu/zeno/papers/humming/humming.pdf): This is paper in 2019 is a recent paper about the topic quey-by-humming.
* Some thoughts:
  * The technological scope of this project is wider than others because it involves the work of database, query search, while including the feature extraction task that every other projects have.
  * The natural of this problem on its own is simpler because Roblox ask us to have 

## 5. Good music in games (royalty free)
* Similar to the `Automatic Music Generation with Features task`

## 6. Sentiment analysis of user experience for developers
* Similar to the `Music Sentiment Analysis task`

## 7. Add sound effects according to speech recognition/text
* Similar to the `Automatic Music Generation with Features task`

## 8. Personality from speech:
1. Similar to the `Music Sentiment Analysis task`
2. Resources:
   * [https://www.researchgate.net/publication/224193151_Automatically_Assessing_Personality_from_Speech](https://www.researchgate.net/publication/224193151_Automatically_Assessing_Personality_from_Speech)

## 9. VR support being revived and would allow guesture detection
* This is `[Action Recognition task]` and we can just process the start/stop/pause/etc. of music when an action is detected and recognized.

## 10. Better accessibility support for visual problems, so audio only game: The Vale - Shadow of the Crown
* This is the `[Speech Recognition task]`