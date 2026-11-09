# 지원과제 현황판 바로가기

https://zeronepatent.github.io/gov-projects/ 로 접속하면 지원과제 현황판(Google Apps Script 웹앱)으로 이동합니다.

- 접속은 허용된 계정만 가능합니다(앱의 `사용자` 목록으로 관리).
- 앱을 Google 로그인 정보를 보내지 않는 틀(`credentialless` iframe)에 넣어, 브라우저에 Google 계정이 여러 개여도 열립니다.
- 앱 로그인 토큰과 화면 상태는 이 페이지(zeronepatent.github.io)의 저장소에 맡겨 둡니다.
- 앱 배포 ID가 바뀌면 `index.html`의 `APP` 주소를 고칩니다.
- 아이콘: `icon.svg`가 원본(관공서 + 단계 타임라인). PNG는 `python scripts/make-icons.py`로 다시 만든다.
