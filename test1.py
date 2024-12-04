L1 = [
    "Do you often feel overwhelmed by schoolwork or assignments?",
    "Do you frequently feel anxious about upcoming exams or tests?",
    "Do you find it difficult to relax after a long day at school or after homework?",
    "Do you often feel pressure to meet others’ expectations (from teachers, friends, or family)?",
    "Do you feel stressed about fitting in with your friends or social groups?",
    "Do you experience difficulty sleeping because you're thinking about school or other concerns?",
    "Do you feel like you have too much on your plate and can’t manage everything?",
    "Do you often worry about your future (e.g., college, career, life after school)?",
    "Do you experience physical symptoms like headaches, stomachaches, or tension from stress?",
    "Do you often feel that you don’t have enough time to do everything you want to do?",
    "Do you often feel disconnected or lonely, even when you're surrounded by others?",
    "Do you find yourself procrastinating on assignments or tasks because you feel anxious about them?",
    "Do you feel like you don’t have enough support from family, friends, or teachers when you're stressed?",
    "Do you feel like your stress impacts your mental health or mood on a regular basis?",
    "Do you often feel a sense of dread or anxiety before going to school or facing a challenging situation?"
]
#L1 is for 12-14

L2 = [
    "How frequently do you feel overwhelmed with schoolwork or other responsibilities?",
    "How would you rate the level of pressure you feel to do well in school?",
    "How often does social media contribute to your stress levels?",
    "How much stress do you feel about maintaining friendships or social connections?",
    "How much does your family life contribute to your stress?",
    "How often do family responsibilities (like chores or helping out at home) add to your stress?",
    "When you’re stressed, do you usually talk to someone about it?",
    "How often do you experience physical symptoms (headaches, fatigue, etc.) when stressed?",
    "When you're stressed, how much does it affect your mood?",
    "How often does stress affect your ability to concentrate or focus on tasks?",
    "How confident are you that things will get less stressful as you get older?",
    "How much do you feel adults (teachers, parents, etc.) understand your stress?",
    "How often do you feel pressure to succeed in school to meet family expectations?",
    "How much stress do you feel about your academic performance affecting your future (e.g., college, job prospects)?",
    "When you’re stressed, how much does it affect your sleep?"
]#L2 IS FOR 15-17 questions
L3=[
    'How often do you feel unable to manage your emotions during challenging situations?',
    'Do you find yourself feeling pessimistic or hopeless about the future?',
    'How often do you struggle to find joy in activities you used to enjoy?',
    'Do you experience unexplained fatigue even after getting sufficient sleep?',
    'How often do you notice physical tension, such as clenched jaw or stiff shoulders?',
    'Have you experienced unusual changes in your heart rate or breathing when stressed?',
    'How often do you avoid tasks or responsibilities because they feel overwhelming?',
    'Do you find it hard to stay organized or meet deadlines due to stress?',
    'How often do you overcommit to activities, leaving little time for rest?',
    'Do you frequently forget things or feel mentally "foggy"?',
    'How often do you overthink situations or feel stuck in a loop of negative thoughts?',
    'Do you struggle to make decisions because of feelings of uncertainty or stress?',
    'How often do you feel like withdrawing from social situations or avoiding people?',
    'Do you feel misunderstood or unsupported by those around you when stressed',
    'How often do you feel like your coping strategies are ineffective in managing stress?'
]#L3 IS FOR 18-26 questions

L4 = [
    "How often do you feel overwhelmed by your responsibilities?",
    "Do you experience frequent feelings of anxiety, irritability, or sadness?",
    "Have you recently lost interest in activities you usually enjoy?",
    "Do you often feel tired or fatigued, even after sufficient rest?",
    "Have you noticed changes in your sleep patterns, such as difficulty falling or staying asleep?",
    "Do you experience frequent headaches, muscle tension, or stomach discomfort?",
    "Do you feel like work-related stress is affecting your personal life?",
    "Are you satisfied with the time you have for yourself, hobbies, or relaxation?",
    "Do you have someone you can turn to when you’re feeling stressed or overwhelmed?",
    "Are you experiencing conflicts or challenges in your relationships that add to your stress?",
    "How often do you rely on unhealthy coping mechanisms (e.g., overeating, smoking, excessive screen time)?",
    "Do you feel confident in your ability to manage stress and bounce back from challenges?",
    "Are financial concerns a significant source of stress for you?",
    "Do you feel like you’re making progress toward your personal or professional goals?",
    "How often do you feel a sense of purpose or fulfillment in your life?"
]
#L4 IS FOR 27-37 questions
L5 = [
    "How often do you feel like you're 'burning out' from your responsibilities?",
    "Do you find it difficult to relax, even when you have free time?",
    "How confident are you in your ability to manage unexpected or urgent stressful situations?",
    "How do you typically feel after facing a stressful situation?",
    "Do you feel supported by the people around you when you're stressed?",
    "How often do you engage in activities that help you relax or reduce stress (e.g., exercise, meditation, hobbies)?",
    "Do you have a regular routine for managing stress (e.g., meditation, exercise, journaling)?",
    "How much do you feel in control of your daily life and routines?",
    "Do you feel like you have enough time for yourself outside of work, school, and other obligations?",
    "What is the primary source of your stress?",
    "How satisfied are you with your current work/school-life balance?",
    "When you feel stressed, what is your typical reaction?",
    "How often do you experience physical symptoms of stress (e.g., headaches, fatigue, muscle tension)?",
    "How often do you feel overwhelmed or stressed during a typical week?"
]
#L5 IS FOR 38-45 questions
L6 = [
    "Do you often feel overwhelmed by your responsibilities at work or home?",
    "Do you frequently experience difficulty sleeping due to racing thoughts or anxiety?",
    "Do you find it hard to relax even when you have free time?",
    "Do you feel physically tense or have frequent muscle aches or headaches?",
    "Are you often unable to switch off from work or personal concerns?",
    "Do you have frequent mood swings or irritability due to stress?",
    "Do you feel like you are constantly juggling too many tasks at once?",
    "Do you regularly worry about your financial situation or future security?",
    "Do you feel that you have little time for self-care or personal hobbies?",
    "Do you find it difficult to concentrate or focus on tasks due to stress?",
    "Do you feel like you're always behind or running out of time to get things done?",
    "Do you frequently feel emotionally drained after social events or work meetings?",
    "Do you struggle to find balance between work, family, and personal time?",
    "Do you often turn to unhealthy coping mechanisms (like overeating or drinking) when stressed?",
    "Do you have trouble saying 'no' to requests or taking on too much work or responsibility?"
]

f=open(r'C:\Users\Admin\Desktop\questions.txt','w')
f.write('\n'+'12-14'+'\n'+'\n')
for i in L1:
    f.write(i+'\n')
f.write('\n'+'15-17'+'\n'+'\n')
for i in L2:
    f.write(i+'\n')
f.write('\n'+'18-26'+'\n'+'\n')
for i in L3:
    f.write(i+'\n')
f.write('\n'+'27-37'+'\n'+'\n')
for i in L4:
    f.write(i+'\n')
f.write('\n'+'38-45'+'\n'+'\n')
for i in L5:
    f.write(i+'\n')
f.write('\n'+'46-60'+'\n'+'\n')
for i in L6:
    f.write(i+'\n')
f.close()

S1 = [
    "Your stress test results indicate that you are experiencing normal stress levels.",
    "This means you’re effectively managing the challenges in your life, and your stress is at a healthy, balanced level.",
    "Keep up the good work by maintaining your current habits and coping mechanisms to stay in this positive range!"
]


S2 = [
    "Time Management:",
    "Use planners or apps to organize tasks.",
    "Prioritize and delegate responsibilities where possible.",
    
    "Relaxation Techniques:",
    "Practice deep breathing: Inhale for 4 seconds, hold for 7 seconds, exhale for 8 seconds.",
    "Engage in mindfulness or meditation for 10–15 minutes daily.",
    
    "Physical Activity:",
    "Incorporate regular exercise like yoga, walking, or light cardio. Aim for 30 minutes a day.",
    
    "Social Support:",
    "Spend time with friends or family to talk about your feelings.",
    "Join support groups or clubs to connect with others.",
    
    "Hobby Engagement:",
    "Dedicate time to creative or relaxing activities like painting, reading, or gardening.",
    
    "Dietary Adjustments:",
    "Reduce caffeine, sugar, and processed food.",
    "Opt for whole grains, fruits, and leafy greens to boost mental health."
]

S3 = [
    "Professional Help:",
    "Seek therapy or counseling to identify stressors and develop coping strategies.",
    "Cognitive Behavioral Therapy (CBT) can be highly effective for stress management.",
    
    "Stress Journaling:",
    "Write down your stress triggers and what helps you to get better. Reflect on what you can control.",
    
    "Physical Health:",
    "Include cardio-exercises, such as running or swimming, to release built-up tension.",
    "Ensure 7–8 hours of quality sleep; use calming rituals like herbal tea or white noise.",
    
    "Relaxation Practices:",
    "Explore progressive muscle relaxation: Tense and relax each muscle group sequentially.",
    "Consider aromatherapy with calming essential oils like lavender or chamomile.",
    
    "Boundary Setting:",
    "Learn to say 'no' to avoid overcommitting.",
    "Create work-life separation by setting clear boundaries (e.g., no emails after work hours).",
    
    "Mind-Body Practices:",
    "Try pilates to integrate mental and physical relaxation.",
    "Engage in guided meditations or apps like Headspace or Calm.",
    
    "Medical Evaluation:",
    "Check for underlying issues like hormonal imbalances or nutrient deficiencies that may amplify stress."
]

f=open(r'C:\Users\Admin\Desktop\solutions.txt','w')
for i in S1:
    f.write(i+'\n')
f.write('\n'+'\n')
for i in S2:
    f.write(i+'\n')
f.write('\n'+'\n')
for i in S3:
    f.write(i+'\n')
f.close()
