Q: sha256으로 암호화했을때 다이제스트를 역으로 추적할 수 있는데 추가적으로 난수형 salt를 생성해줘야하나요~? A: SHA256으로 했을때는 여태 알려진 바로는 역으로 추척할 수가 없지만, 그 이외의 약한 해시함수들 MD5 나 SHA-0 SHA-1등을 생성시 salt를 넣어주면 더 강한 암호화가 됩니다.

Q: 해시함수는 공백 한칸과 두칸이 다르게 결과값이 나오나요? A: 네 다르게 나옵니다. 그래서 원본 값등을 검사하는 무결성등을 검사할때 많이 쓰입니다.

Q: 일반적으로 해시 처리를 할 때 해시충돌 가능성을 염두해두고 처리를 하나용? A: 보통 SHA256, (SHA3계열)keccak256등을 알려진 바로 해시충돌은 없습니다. 하지만 MD5나 SHA-0 SHA-1등은 해시충돌이 밝혀졌기 때문에 실무에서 사용하지 않습니다.  더 염려가 되면 시간과 비용이 조금 더 드는 256비트 이상인 512정도로 하시면 됩니다.

Q: Java에서 null 방지 꿀팁이 또 있을까요? A: 자바8 이상부터는 Optional이라는 것이 생겼습니다. 그것을 적극 활용하시면 null Exception을 회피 하실수 있으실 껍니다.

Q: java말고 python에서의 시큐어코딩 강의도 진행될까요? A: 네 언제 한번 시간을 잡아서 기획해 보도록 하겠습니다.

Q: Optional도 null 방지의 한가지이지 않나요? A: 네 맞습니다. JAVA버전8 이상부터 나왔습니다.

Q: sql 인젝션은 매년 owasp 보안취약점 1위로 선정되던데 매직쿼터를 막아주면 어떤 방법으로 공격하나요? A: 싱글쿼터를 말씀하시는거 같은데, 그이외에도 주석 및 논리부정등으로 공격할 수 있습니다.