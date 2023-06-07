import random

quote = [
    ["'Any fool can know. The point is to understand.' \n- Albert Einstein -"],
    [
        "'The illiterate of the 21st century will not be those who cannot read and write, but those who cannot learn, unlearn, and relearn.' \n- Alvin Toffler -"
    ],
    ["'You aren't learning anything when you're talking.' \n- Lyndon B. Johnson -"],
    [
        "'Enlightenment is man's leaving his self-caused immaturity. Immaturity is the incapacity to use one's intelligence without the guidance of another. Such immaturity is self-caused if it is not caused by lack of intelligence, but by lack of determination and courage to use one's intelligence without being guided by another. Sapere Aude! Have the courage to use your own intelligence! is therefore the motto of the enlightenment.' \n- Immanuel Kant -"
    ],
    [
        "'The more I read, the more I acquire, the more certain I am that I know nothing.' \n- Voltaire -"
    ],
    [
        "'Don't just teach your children to read. Teach them to question what they read. Teach them to question everything.' \n- George Carlin -"
    ],
    [
        "'A man who reads too much and uses his own brain too little falls into lazy habits of thinking.' \n- Albert Einstein -"
    ],
    [
        "'We must learn to live together as brothers or perish together as fools.' \n- Martin Luther King Jr. -"
    ],
    [
        "'All of the books in the world contain no more information than is broadcast as video in a single large American city in a single year. Not all bits have equal value.' \n- Carl Sagan -"
    ],
    [
        "'There are four powers: memory and intellect, desire and covetousness. The two first are mental and the others sensual. The three senses sight, hearing, and smell cannot well be prevented; touch and taste not at all.' \n- Leonardo da Vinci -"
    ],
    [
        "'There is no end to education. It is not that you read a book, pass an examination, and finish with education. The whole of life, from the moment you are born to the moment you die, is a process of learning.' \n- Jiddu Krishnamurti -"
    ],
    [
        "'I am always ready to learn although I do not always like being taught.' \n- Winston Churchill -"
    ],
    [
        "'Live as if you were to die tomorrow. Learn as if you were to live forever.' \n- Mahatma Gandhi -"
    ],
    [
        "'Wisdom is not a product of schooling but of the lifelong attempt to acquire it.' \n- Albert Einstein -"
    ],
    [
        "'Tell me and I forget, teach me and I may remember, involve me and I learn.' \n- Benjamin Franklin -"
    ],
    [
        "'One hour per day of study in your chosen field is all it takes. One hour per day of study will put you at the top of your field within three years. Within five years you'll be a national authority. In seven years, you can be one of the best people in the world at what you do.' \n- Earl Nightingale -"
    ],
    [
        "'Research shows that you begin learning in the womb and go right on learning until the moment you pass on. Your brain has a capacity for learning that is virtually limitless, which makes every human a potential genius.' \n- Michael J. Gelb -"
    ],
    [
        "'Anyone who stops learning is old, whether at 20 or 80. Anyone who keeps learning stays young. The greatest thing in life is to keep your mind young.' \n- Henry Ford -"
    ],
    [
        "'Study hard what interests you the most in the most undisciplined, irreverent and original manner possible.' \n- Richard Feynman -"
    ],
    [
        "'True teachers are those who use themselves as bridges over which they invite their students to cross; then, having facilitated their crossing, joyfully collapse, encouraging them to create their own.' \n- Nikos Kazantzakis -"
    ],
    [
        "'There is divine beauty in learning…. To learn means to accept the postulate that life did not begin at my birth. Others have been here before me, and I walk in their footsteps.' \n- Elie Wiesel -"
    ],
    ["'Curiosity is the wick in the candle of learning.' \n- William Arthur Ward -"],
    [
        "'Education is the ability to listen to almost anything without losing your temper or your self-confidence.' \n- Robert Frost -"
    ],
    [
        "'Learning is not attained by chance. It must be sought for with ardour and attended with diligence.' \n- Abigail Adams -"
    ],
    [
        "'Being a student is easy. Learning requires actual work.' \n- William Crawford -"
    ],
    [
        "'If you think education is expensive, try estimating the cost of ignorance.' \n- Howard Gardner -"
    ],
    [
        "'I realized that becoming a master of karate was not about learning 4,000 moves but about doing just a handful of moves 4,000 times.' \n- Chet Holmes -"
    ],
    [
        "'The key to pursuing excellence is to embrace an organic, long-term learning process, and not to live in a shell of static, safe mediocrity. Usually, growth comes at the expense of previous comfort or safety.' \n- Josh Waitzkin -"
    ],
    [
        "'The beautiful thing about learning is that nobody can take it away from you.' \n- B.B. King -"
    ],
    [
        "'Learning is a treasure that will follow its owner everywhere.' \n- Chinese Proverb -"
    ],
    [
        "'The only person who is educated is the one who has learned how to learn and change.' \n- Carl Rogers -"
    ],
    [
        "'The more I read, the more I acquire, the more certain I am that I know nothing.' \n- Voltaire -"
    ],
    [
        "'Study hard what interests you the most in the most undisciplined, irreverent and original manner possible.' \n- Richard Feynman -"
    ],
    [
        "'Self-education is, I firmly believe, the only kind of education there is.' \n- Isaac Asimov -"
    ],
    ["'Study the past if you would define the future.' \n- Confucius -"],
    [
        "'Education is the passport to the future, for tomorrow belongs to those who prepare for it today.' \n- Malcolm X -"
    ],
    [
        "'Education is the most powerful weapon which you can use to change the world.' \n- Nelson Mandela -"
    ],
    [
        "'As we look ahead into the next century, leaders will be those who empower others.' \n- Bill Gates -"
    ],
    [
        "'That is what learning is. You suddenly understand something you've understood all your life, but in a new way.' \n- Doris Lessing -"
    ],
    [
        "'No thief, however skillful, can rob one of knowledge, and that is why knowledge is the best and safest treasure to acquire.' \n- L. Frank Baum -"
    ],
    [
        "'Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do.' \n- Pele -"
    ],
    [
        "'The purpose of learning is growth, and our minds, unlike our bodies, can continue growing as we continue to live.' \n- Mortimer Adler -"
    ],
    [
        "'Continuous learning is the minimum requirement for success in any field.' \n- Brian Tracy -"
    ],
    [
        "'A ‘genius' is often merely a talented person who has done all of his or her homework.' \n- Thomas Edison -"
    ],
    [
        "'To attain knowledge, add things every day. To attain wisdom, remove things every day.' \n- Lao Tzu -"
    ],
    [
        "'Learning life's lessons is not about making your life perfect, but about seeing life as it was meant to be.' ― Elisabeth Kubler-Ross -"
    ],
    ["'If you learn from defeat, you haven't really lost.' \n- Zig Ziglar -"],
    ["'Learn continually. There's always “one more thing” to learn.' \n- Steve Jobs -"],
    [
        "'I hear and I forget. I see and I remember. I do and I understand.' \n- Confucius -"
    ],
    [
        "'Anyone who has never made a mistake has never tried anything new.' \n- Albert Einstein -"
    ],
    [
        "'A man only learns in two ways, one by reading, and the other by association with smarter people.' \n- Will Rogers -"
    ],
    [
        "'If you want to increase your success rate, double your failure rate.' \n- Thomas J. Watson -"
    ],
    [
        "'It is what we know already that often prevents us from learning.' \n- Claude Bernard -"
    ],
    [
        "'Power corrupts. Knowledge is power. Study hard. Be evil.' \n- Eleanor Roosevelt -"
    ],
    [
        "'Mathematics is the language with which God has written the universe.' \n- Galileo Galilei -"
    ],
    [
        "'Learning is not attained by chance, it must be sought for with ardor and diligence.' \n- Abigail Adams -"
    ],
    [
        "'Common sense is the collection of prejudices acquired by age eighteen.' \n- Albert Einstein -"
    ],
    [
        "'A teacher who is attempting to teach without inspiring the pupil with a desire to learn is hammering on cold iron.' \n- Horace Mann -"
    ],
    [
        "'Knowledge has to be improved, challenged, and increased constantly, or it vanishes.' \n- Peter Drucker -"
    ],
    [
        "'All the world is my school and all humanity is my teacher.' \n- George Whitman -"
    ],
    [
        "'I am quite correctly described as ‘more of a sponge than an inventor….' \n- Thomas Edison -"
    ],
    [
        "'The best thing a human being can do is to help another human being know more.' \n- Charlie Munger -"
    ],
    [
        "'Education is learning what you didn't even know you didn't know.' \n- Daniel Boorstin -"
    ],
    [
        "'Formal education will make you a living. Self-education will make you a fortune.' \n- Jim Rohn -"
    ],
    [
        "'The whole purpose of education is to turn mirrors into windows.' \n- Sydney J. Harris -"
    ],
    [
        "'If you only read the books that everyone else is reading, you can only think what everyone else is thinking.' \n- Haruki Murakami -"
    ],
    ["'The roots of education are bitter, but the fruit is sweet.' \n- Aristotle -"],
    [
        "'The more that you read, the more things you will know, the more that you learn, the more places you'll go.' \n- Dr. Seuss -"
    ],
    [
        "'Education without values, as useful as it is, seems rather to make man a more clever devil.' \n- C.S. Lewis -"
    ],
    ["'The learning process continues until the day you die.' \n- Kirk Douglas -"],
    [
        "'Education is not the filling of a pail, but the lighting of a fire.' \n- W.B. Yeats -"
    ],
    [
        "'Develop a passion for learning. If you do, you will never cease to grow.' \n- Anthony J. D'Angelo -"
    ],
    [
        "'Education is not preparation for life; education is life itself.' \n- John Dewey -"
    ],
    [
        "'Knowledge is power. Information is liberating. Education is the premise of progress, in every society, in every family.' \n- Kofi Annan -"
    ],
    [
        "'A person who won't read has no advantage over one who can't read.' \n- Mark Twain -"
    ],
    [
        "'Upon the subject of education… I can only say that I view it as the most important subject which we as a people may be engaged in.' \n- Abraham Lincoln -"
    ],
    [
        "'Learning is like rowing upstream: not to advance is to drop back.' \n- Chinese proverb -"
    ],
    [
        "'It is as impossible to withhold education from the receptive mind as it is impossible to force it upon the unreasoning.' \n- Agnes Repplier -"
    ],
    [
        "'They cannot stop me. I will get my education, if it is in the home, school, or anyplace.' \n- Malala Yousafzai -"
    ],
    [
        "'Learning is not the product of teaching. Learning is the product of the activity of learners.' \n- John Holt -"
    ],
    [
        "'Take the attitude of a student, never be too big to ask questions, never know too much to learn something new.' \n- Og Mandino -"
    ],
    [
        "'I agree that a love of reading is a great gift for a parent to pass on to his or her child.' \n- Ann Brashares -"
    ],
    [
        "'Intelligence plus character-that is the goal of true education.' \n- Martin Luther King Jr. -"
    ],
    [
        "'Education is for improving the lives of others and for leaving your community and world better than you found it.' \n- Marian Wright Edelman -"
    ],
    [
        "'Every act of conscious learning requires the willingness to suffer an injury to one's self-esteem. That is why young children, before they are aware of their own self-importance, learn so easily.' \n- Thomas Szasz -"
    ],
    [
        "'You are always a student, never a master. You have to keep moving forward.' \n- Conrad Hall -"
    ],
    [
        "'Children have to be educated, but they have also to be left to educate themselves.' \n- Ernest Dimnet -"
    ],
    ["'Education consists mainly of what we have unlearned.' \n- Mark Twain -"],
    [
        "'Wisdom…. comes not from age, but from education and learning.' \n- Anton Chekhov -"
    ],
    [
        "'Education is a continual process, it's like a bicycle… If you don't pedal you don't go forward.' \n- George Weah -"
    ],
    [
        "'Education is not the filling of a pail, but the lighting of a fire.' \n- William Butler Yeats -"
    ],
]


def get_quote():
    return quote[random.randint(0, len(quote) - 1)][0]
