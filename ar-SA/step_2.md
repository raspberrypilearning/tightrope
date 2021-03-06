## ارسم مسار

دعنا أولاً نرسم المسار الذي يجب أن تتبعه شخصيتك.

+ افتح مشروع حبل البهلوان مشروع البداية بالTrinket: <a href="http://jumpto.cc/tightrope-go" target="_blank">jumpto.cc/tightrope-go</a>.
    
    **تم اعداد التعليمات البرمجية لإعداد Sense HAT لك.**

+ لنبدأ بإنشاء متغيرات لتخزين الألوان التي تريد استخدامها. تذكر أنه لتعيين لون للضوء الواحد، يجب أن تقول كم يجب أن يكون لديه اللون الأحمر والأخضر والأزرق.
    
    لإنشاء اللون الأصفر ، ستحتاج إلى الحد الأقصى باللون الأحمر والأخضر ، ولا يوجد أزرق:
    
    ![لقطة الشاشة](images/tightrope-yellow.png)
    
    (إذا كنت تفضل ذلك ، يمكنك الانتقال إلى [jumpto.cc/colours](http://jumpto.cc/colours) واختر أي لون يعجبك!

+ ستحتاج أيضًا إلى وحدات بكسل سوداء (أو أي لون تريده) حول المسار.
    
    ![لقطة الشاشة](images/tightrope-black.png)

+ لرسم المسار الخاص بك ، تحتاج أولاً إلى إنشاء قائمة تحتوي على لون كل بكسل.
    
    ![لقطة الشاشة](images/tightrope-path.png)
    
    **لتقليل الكتابة، يمكنك نسخ قوس قزح من `snippets.py` في مشروعك.**
    
    ![لقطة الشاشة](images/tightrope-snippets.png)

+ بعد ذلك ، تحتاج إلى استدعاء `set_pixels` لعرض صورة مسارك على Sense HAT.
    
    ![لقطة الشاشة](images/tightrope-set-pixels.png)

+ انقر فوق 'تشغيل' لاختبار الكود الخاص بك. يجب أن ترى بكسل أصفر في الأماكن التي استخدمت المتغير `y` ، ولايوجد لون في الأماكن التي استخدمتها `x`.
    
    ![لقطة الشاشة](images/tightrope-path-test.png)