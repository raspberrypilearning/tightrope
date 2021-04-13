## परिचय:

इस प्रोजेक्ट में आप एक गेम बनाएँगे जिसमें आपको पात्र का किसी रास्ते पर मार्गदर्शन करने के लिए अपने Sense HAT को झुकाना होगा। यदि आप रास्ते से हट जाते हैं, तो आपको शुरुआत से फिर से शुरू करना होगा!

<div class="trinket">
  <iframe src="https://trinket.io/embed/python/790adaa749?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen mark="crwd-mark">
</iframe> <img src="images/tightrope-final.png" />
</div>

### क्लब लीडरों के लिए अतिरिक्त जानकारी

यदि आप इस प्रोजेक्ट को प्रिंट करना चाहते हैं, तो कृपया [प्रिंटर अनुकूल संस्करण](https://projects.raspberrypi.org/en/projects/tightrope/print) का उपयोग करें।

## \--- collapse \---

## title: क्लब नेता नोट

## परिचय:

इस प्रोजेक्ट में, बच्चे लाइन का अनुसरण करने वाली गेम बनाकर Sense HAT ओरिएंटेशन सेंसर के बारे में सीखेंगे। खिलाड़ी पात्र को किसी रास्ते पर चलाने के लिए Sense HAT को झुकाता है। रास्ते से हटने पर खिलाड़ी को वापस स्टार्ट पर भेज दिया जाता है!

## ऑनलाइन संसाधन

**इस प्रोजेक्ट में Python 3 का उपयोग किया जाता है।** Python को ऑनलाइन लिखने के लिए हम [Trinket](https://trinket.io/) का उपयोग करने की सलाह देते हैं। इस प्रोजेक्ट में निम्नलिखित Trinket हैं:

* ['ट्राइट्रोप' स्टार्टर ट्रिंकेट - jumpto.cc/tightrope-go](http://jumpto.cc/tightrope-go)

एक ऐसा trinket भी है जिसमें पूर्ण किया गया प्रोजेक्ट है:

* ['Tightrope' समाप्त - trinket.io/python/790adaa749](https://trinket.io/python/790adaa749)

## ऑफ़लाइन संसाधन

इस प्रोजेक्ट को Sense HAT से किसी Raspberry Pi कंप्यूटर पर [ऑफ़लाइन भी पूरा किया जा सकता है](https://www.codeclubprojects.org/en-GB/resources/physical-sense-hat/)। आप इस प्रोजेक्ट के लिए 'प्रोजेक्ट सामग्री' लिंक पर क्लिक करके प्रोजेक्ट के संसाधनों पर पहुँच प्राप्त कर सकते हैं। इस लिंक में 'प्रोजेक्ट संसाधन' खंड है, जिसमें ऐसे संसाधन सम्मिलित हैं जिसकी बच्चों को इस प्रोजेक्ट को ऑफ़लाइन पूरा करने की ज़रूरत होगी। सुनिश्चित करें कि प्रत्येक बच्चे को इन संसाधनों की प्रतिलिपि तक पहुँच प्राप्त होती है। इस खंड में निम्नलिखित फाइलें शामिल हैं:

* tightrope/main.py
* tightrope/snippets.py

आपको 'स्वयंसेवक संसाधन' खंड में इस प्रोजेक्ट का पूर्ण किया गया संस्करण भी मिल सकता है, जिसमें निम्न शामिल हैं:

* tightrope-finished/main.py
* tightrope-finished/snippets.py

(उपर्युक्त सभी संसाधन प्रोजेक्ट और स्वयंसेवक `.zip` फ़ाइलों के रूप में भी डाउनलोड किए जा सकते हैं।)

## सीखने के उद्देश्य

* Sense HAT ओरिएंटेशन (roll, pitch और yaw);
* Sense HAT डिस्प्ले;
* RGB रंग;

इस प्रोजेक्ट में [Raspberry Pi डिजिटल निर्माण पाठ्यक्रम](http://rpf.io/curriculum) के निम्नलिखित पहलुओं के तत्व सम्मिलित हैं:

* [किसी समस्या को हल करने के लिए प्रोग्रामिंग संरचनाओं को जोड़ें।](https://www.raspberrypi.org/curriculum/programming/builder)

## चुनौतियाँ

* "अपना खुद का रास्ता बनाना" - पिक्सेल की सूची का उपयोग करके एक छवि बनाना;
* "ऊपर ले जाना!" - `roll` मानों को बदलने की प्रतिक्रिया के रूप में पात्र को ऊपर ले जाना।
* "कठिनाई को बदलना" - समाप्त गेम का परीक्षण करना और खिलाड़ी की प्रतिक्रिया के आधार पर परिवर्तन करना।

\--- /collapse \---

## \--- collapse \---

## title: प्रोजेक्ट सामग्री

## प्रोजेक्ट संसाधन

* [सभी प्रोजेक्ट संसाधनों वाली .zip फ़ाइल](resources/tightrope-project-resources.zip)
* [Tightrope स्टार्टर प्रोजेक्ट](http://jumpto.cc/tightrope-go)
* [ऑफ़लाइन स्टार्टर Python फ़ाइल](resources/tightrope-main.py)
* [ऑफ़लाइन Python फ़ाइल जिसमें उपयोगी कोड होते हैं](resources/tightrope-snippets.py)

## क्लब लीडर संसाधन

* [सभी प्रोजेक्ट संसाधनों वाली .zip फ़ाइल](resources/tightrope-volunteer-resources.zip)
* [ऑनलाइन पूर्ण Trinket Tightrope प्रोजेक्ट](https://trinket.io/python/790adaa749)
* [tightrope-finished/main.py](resources/tightrope-finished-main.py)
* [tightrope-finished/snippets.py](resources/tightrope-finished-snippets.py)

\--- /collapse \---