<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>수학 & 진로 상담실 | 실시간 상담 예약 및 피드백 조회</title>
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <!-- Google Fonts: Pretendard alternative Noto Sans KR & JetBrains Mono for numbers -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@500;700&family=Noto+Sans+KR:wght@400;500;600;700&display=swap" rel="stylesheet">
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css" />
  <!-- Google Identity Services (Google Sign-In) -->
  <script src="https://accounts.google.com/gsi/client" async defer></script>

  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Noto Sans KR"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          },
          colors: {
            cream: {
              50: '#FDFBF7',
              100: '#F7F3EB',
              200: '#EFE8D8',
            },
            sage: {
              50: '#F2F7F4',
              100: '#E1EDE6',
              500: '#3B7A57',
              600: '#2E6346',
              700: '#234D36',
            },
            amberWarm: {
              50: '#FFFBEB',
              100: '#FEF3C7',
              500: '#D97706',
              600: '#B45309',
            }
          }
        }
      }
    }
  </script>

  <style>
    body {
      background-color: #FAF7F2;
      background-image: 
        radial-gradient(#E5DEC9 1px, transparent 1px),
        linear-gradient(to right, rgba(229, 222, 201, 0.25) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(229, 222, 201, 0.25) 1px, transparent 1px);
      background-size: 24px 24px, 48px 48px, 48px 48px;
      color: #292524;
    }

    @keyframes softPulse {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.06); opacity: 0.75; }
    }
    .pulse-badge {
      animation: softPulse 2.4s infinite ease-in-out;
    }

    .custom-scroll::-webkit-scrollbar {
      width: 6px;
    }
    .custom-scroll::-webkit-scrollbar-track {
      background: #F5F2EB;
      border-radius: 9999px;
    }
    .custom-scroll::-webkit-scrollbar-thumb {
      background: #D6CFC2;
      border-radius: 9999px;
    }

    @media print {
      body * {
        visibility: hidden;
      }
      #printReportSection, #printReportSection * {
        visibility: visible;
      }
      #printReportSection {
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        margin: 0;
        padding: 20px;
        background: white !important;
        border: none !important;
        box-shadow: none !important;
      }
      .no-print {
        display: none !important;
      }
    }
  </style>
</head>

<body class="min-h-screen flex flex-col selection:bg-amber-200 selection:text-stone-900 overflow-x-hidden">

  <div id="toastContainer" class="fixed top-5 right-5 z-50 flex flex-col gap-2 pointer-events-none"></div>

  <header class="sticky top-0 z-30 backdrop-blur-md bg-[#FAF7F2]/90 border-b border-stone-200/80 shadow-sm">
    <div class="max-w-6xl mx-auto px-4 sm:px-6 py-3.5 flex flex-wrap items-center justify-between gap-3">
      <!-- Brand / Room Name -->
      <div class="flex items-center gap-3">
        <div class="w-11 h-11 rounded-2xl bg-sage-600 text-white flex items-center justify-center shadow-sm font-mono font-bold text-xl">
          ∑
        </div>
        <div>
          <div class="flex items-center gap-2">
            <span class="text-xs font-semibold tracking-wider uppercase px-2 py-0.5 rounded-full bg-amber-100 text-amber-800 border border-amber-200">
              2026학년도 2학기 정기 상담
            </span>
            <span id="liveClock" class="text-xs font-mono text-stone-500 hidden sm:inline-block"></span>
          </div>
          <h1 class="text-lg sm:text-xl font-bold text-stone-800 tracking-tight mt-0.5">
            수학 선생님과 함께하는 <span class="text-sage-600">진로·학업 상담실</span>
          </h1>
        </div>
      </div>

      <!-- Right Controls: Role Switcher -->
      <div class="flex items-center gap-2 sm:gap-3 ml-auto">
        <div class="bg-stone-200/80 p-1 rounded-xl flex items-center text-xs sm:text-sm font-semibold">
          <button id="btnStudentRole" onclick="switchRoleMode('student')"
            class="px-3 py-1.5 rounded-lg bg-white text-stone-900 shadow-sm transition flex items-center gap-1.5">
            <i class="fa-solid fa-graduation-cap text-sage-600"></i>
            <span>학생 화면</span>
          </button>
          <button id="btnTeacherRole" onclick="requestTeacherLogin()"
            class="px-3 py-1.5 rounded-lg text-stone-600 hover:text-stone-900 transition flex items-center gap-1.5">
            <i class="fa-solid fa-chalkboard-user text-amber-600"></i>
            <span>선생님 관리</span>
          </button>
        </div>
      </div>
    </div>
  </header>

  <main class="flex-1 max-w-6xl w-full mx-auto px-4 sm:px-6 py-6 sm:py-8 space-y-8">

    <section aria-label="실시간 상담 전광판" class="space-y-3">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
        <div class="flex items-center gap-2.5">
          <span class="relative flex h-3 w-3">
            <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
            <span class="relative inline-flex rounded-full h-3 w-3 bg-emerald-500"></span>
          </span>
          <h2 class="text-base sm:text-lg font-bold text-stone-800">
            실시간 상담 진행 전광판
          </h2>
          <span class="text-xs text-stone-500 bg-stone-200/70 px-2.5 py-0.5 rounded-full">
            장소: 본관 3층 수학과 연구실 옆 상담코너
          </span>
        </div>
        <p class="text-xs text-stone-500">
          <i class="fa-regular fa-bell mr-1 text-amber-600"></i>
          학생은 상담시간에 맞춰서 학년실로 늦거나 못오면 후순위로 밀려나요.
        </p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
        
        <!-- 1. 현재 상담 중 (In Session - 5 Cols) -->
        <div class="lg:col-span-5 bg-gradient-to-br from-sage-600 to-sage-700 text-white rounded-3xl p-5 sm:p-6 shadow-md relative overflow-hidden flex flex-col justify-between min-h-[240px]">
          <div class="absolute -right-4 -bottom-6 text-9xl font-serif text-white/10 select-none pointer-events-none">
            ∫
          </div>

          <div class="flex items-center justify-between">
            <span class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-white/15 backdrop-blur-sm text-xs font-semibold tracking-wide">
              <span class="w-2 h-2 rounded-full bg-emerald-300 animate-pulse"></span>
              현재 상담 중 (IN SESSION)
            </span>
          </div>

          <div id="inSessionBoard" class="my-4">
            <!-- Dynamically populated -->
          </div>

          <div class="pt-3 border-t border-white/15 flex items-center justify-between gap-2 text-xs text-emerald-100">
            <span><i class="fa-solid fa-circle-exclamation mr-1.5 text-amber-300"></i>학년실 상담 코너에서 대기 후 입실하세요.</span>
            <span id="inSessionCountBadge" class="font-mono font-bold shrink-0">1명 진행중</span>
          </div>
        </div>

        <!-- 2. 상담 대기번호 / 대기열 (Waiting Queue - 4 Cols) -->
        <div class="lg:col-span-4 bg-white rounded-3xl p-5 border border-stone-200/90 shadow-sm flex flex-col justify-between min-h-[240px]">
          <div>
            <div class="flex items-center justify-between mb-3">
              <div class="flex items-center gap-2">
                <span class="w-7 h-7 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center font-bold text-sm">
                  <i class="fa-solid fa-clock-rotate-left"></i>
                </span>
                <h3 class="font-bold text-stone-800 text-base">상담 대기 순번</h3>
              </div>
              <span id="waitingCountBadge" class="text-xs font-bold px-2.5 py-1 rounded-full bg-amber-50 text-amber-700 border border-amber-200">
                대기 0명
              </span>
            </div>

            <div id="waitingBoardList" class="space-y-2 max-h-[155px] overflow-y-auto custom-scroll pr-1">
              <!-- Dynamically populated -->
            </div>
          </div>

          <div class="mt-3 pt-2.5 border-t border-stone-100 flex items-center justify-between text-xs text-stone-400">
            <span>예약 확정 학생만 날짜·시간순 표시</span>
            <span class="text-amber-600 font-medium">평균 15~20분 소요</span>
          </div>
        </div>

        <!-- 3. 상담 완료 (Completed - 3 Cols) -->
        <div class="lg:col-span-3 bg-cream-100/90 rounded-3xl p-5 border border-stone-200/80 shadow-sm flex flex-col justify-between min-h-[240px]">
          <div>
            <div class="flex items-center justify-between mb-3">
              <div class="flex items-center gap-2">
                <span class="w-7 h-7 rounded-xl bg-stone-200 text-stone-700 flex items-center justify-center font-bold text-sm">
                  <i class="fa-solid fa-check-double"></i>
                </span>
                <h3 class="font-bold text-stone-800 text-base">상담 완료</h3>
              </div>
              <span id="completedCountBadge" class="text-xs font-semibold px-2.5 py-1 rounded-full bg-stone-200/80 text-stone-700">
                0명 완료
              </span>
            </div>

            <div id="completedBoardList" class="space-y-2 max-h-[155px] overflow-y-auto custom-scroll pr-1">
              <!-- Dynamically populated -->
            </div>
          </div>

          <div class="mt-3 pt-2.5 border-t border-stone-200/70 text-xs text-stone-500 flex items-center justify-between">
            <span>피드백 카드를 조회해 보세요!</span>
            <button onclick="switchStudentTab('inquiry')" class="text-sage-600 font-semibold hover:underline">
              결과 조회 →
            </button>
          </div>
        </div>

      </div>
    </section>

    <section id="studentWorkspace" class="space-y-6">
      
      <div class="bg-stone-200/70 p-1.5 rounded-2xl max-w-md mx-auto grid grid-cols-2 gap-1.5 shadow-inner">
        <button id="tabBtnApply" onclick="switchStudentTab('apply')"
          class="py-3 px-4 rounded-xl font-bold text-sm sm:text-base transition flex items-center justify-center gap-2 bg-white text-stone-900 shadow-sm">
          <i class="fa-solid fa-pen-to-square text-sage-600"></i>
          <span>1. 상담 신청하기</span>
        </button>
        <button id="tabBtnInquiry" onclick="switchStudentTab('inquiry')"
          class="py-3 px-4 rounded-xl font-bold text-sm sm:text-base transition flex items-center justify-center gap-2 text-stone-600 hover:text-stone-900">
          <i class="fa-solid fa-envelope-open-text text-amber-600"></i>
          <span>2. 결과·피드백 조회</span>
        </button>
      </div>

      <!-- TAB 1 CONTENT: 학생 상담 신청 폼 -->
      <div id="tabPanelApply" class="bg-white rounded-3xl border border-stone-200/90 shadow-sm overflow-hidden">
        <div class="grid grid-cols-1 lg:grid-cols-12">
          
          <div class="lg:col-span-4 bg-cream-100 p-6 sm:p-8 border-b lg:border-b-0 lg:border-r border-stone-200/80 flex flex-col justify-between">
            <div class="space-y-4">
              <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sage-100 text-sage-700 text-xs font-bold">
                <i class="fa-solid fa-mug-hot"></i> 따뜻한 수학 상담실 안내
              </div>
              <h3 class="text-xl sm:text-2xl font-bold text-stone-800 leading-snug">
                성적 고민부터 진로까지,<br/>편한 마음으로 신청하세요.
              </h3>
              <p class="text-sm text-stone-600 leading-relaxed">
                수학 공부법이 막막하거나, 내신·수능 준비, 이과 계열 진학, 수학 세특 탐구 주제 등 어떤 이야기든 환영합니다.
              </p>

              <div class="space-y-2.5 pt-2">
                <div class="flex items-start gap-3 p-3 rounded-2xl bg-white/80 border border-stone-200/60">
                  <span class="w-6 h-6 rounded-full bg-sage-600 text-white text-xs font-mono font-bold flex items-center justify-center shrink-0 mt-0.5">1</span>
                  <div class="text-xs text-stone-600">
                    <strong class="text-stone-800 block mb-0.5">희망 시간 & 고민 선택</strong>
                    원하는 시간대와 상담 주제를 선택해 접수합니다.
                  </div>
                </div>
                <div class="flex items-start gap-3 p-3 rounded-2xl bg-white/80 border border-stone-200/60">
                  <span class="w-6 h-6 rounded-full bg-sage-600 text-white text-xs font-mono font-bold flex items-center justify-center shrink-0 mt-0.5">2</span>
                  <div class="text-xs text-stone-600">
                    <strong class="text-stone-800 block mb-0.5">비밀번호 4자리 설정</strong>
                    나만 볼 수 있도록 숫자 4자리 비밀번호를 지정합니다.
                  </div>
                </div>
                <div class="flex items-start gap-3 p-3 rounded-2xl bg-white/80 border border-stone-200/60">
                  <span class="w-6 h-6 rounded-full bg-sage-600 text-white text-xs font-mono font-bold flex items-center justify-center shrink-0 mt-0.5">3</span>
                  <div class="text-xs text-stone-600">
                    <strong class="text-stone-800 block mb-0.5">확정 시간 & 피드백 확인</strong>
                    상담 후 선생님이 남겨주신 맞춤 입시·학습 피드백을 조회합니다.
                  </div>
                </div>
              </div>
            </div>

            <div class="mt-6 pt-4 border-t border-stone-200/80 flex items-center gap-3">
              <div class="w-10 h-10 rounded-full bg-amber-100 text-amber-700 flex items-center justify-center font-bold">
                <i class="fa-solid fa-lightbulb"></i>
              </div>
              <p class="text-xs text-stone-500 leading-normal">
                비밀번호를 잊어버렸다면 언제든 선생님께 말씀해 주세요!
              </p>
            </div>
          </div>

          <form id="counselingApplyForm" onsubmit="handleStudentSubmit(event)" class="lg:col-span-8 p-6 sm:p-8 space-y-6">
            
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label for="inputStudentId" class="block text-sm font-bold text-stone-700 mb-1.5">
                  학번 (5자리) <span class="text-rose-500">*</span>
                </label>
                <div class="relative">
                  <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center text-stone-400">
                    <i class="fa-solid fa-id-badge"></i>
                  </span>
                  <input id="inputStudentId" type="text" maxlength="5" required
                    placeholder="예: 20415 (2학년 4반 15번)"
                    class="w-full pl-10 pr-4 py-3 rounded-xl border border-stone-300 focus:border-sage-600 focus:ring-2 focus:ring-sage-500/20 outline-none font-mono text-sm transition" />
                </div>
              </div>

              <div>
                <label for="inputStudentName" class="block text-sm font-bold text-stone-700 mb-1.5">
                  이름 <span class="text-rose-500">*</span>
                </label>
                <div class="relative">
                  <span class="absolute inset-y-0 left-0 pl-3.5 flex items-center text-stone-400">
                    <i class="fa-solid fa-user"></i>
                  </span>
                  <input id="inputStudentName" type="text" required
                    placeholder="본인 이름을 입력하세요"
                    class="w-full pl-10 pr-4 py-3 rounded-xl border border-stone-300 focus:border-sage-600 focus:ring-2 focus:ring-sage-500/20 outline-none text-sm transition" />
                </div>
              </div>
            </div>

            <div>
              <label class="block text-sm font-bold text-stone-700 mb-2">
                상담 주제 선택 <span class="text-rose-500">*</span>
              </label>
              <div id="topicChipContainer" class="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
                <button type="button" onclick="selectTopic('수학 학습법·성적 고민')" data-topic="수학 학습법·성적 고민"
                  class="topic-chip p-3 rounded-xl border-2 border-sage-600 bg-sage-50 text-sage-700 font-bold text-xs sm:text-sm flex items-center gap-2 transition text-left">
                  <i class="fa-solid fa-square-root-variable text-base"></i>
                  <span>수학 학습법·성적 고민</span>
                </button>
                <button type="button" onclick="selectTopic('내신·수능 선택과목(미적/기하/확통)')" data-topic="내신·수능 선택과목(미적/기하/확통)"
                  class="topic-chip p-3 rounded-xl border border-stone-200 hover:border-stone-300 bg-white text-stone-700 font-medium text-xs sm:text-sm flex items-center gap-2 transition text-left">
                  <i class="fa-solid fa-compass-drafting text-base text-stone-400"></i>
                  <span>선택과목 (미적/기하/확통)</span>
                </button>
                <button type="button" onclick="selectTopic('수학 세특·심화 탐구 주제')" data-topic="수학 세특·심화 탐구 주제"
                  class="topic-chip p-3 rounded-xl border border-stone-200 hover:border-stone-300 bg-white text-stone-700 font-medium text-xs sm:text-sm flex items-center gap-2 transition text-left">
                  <i class="fa-solid fa-book-open-reader text-base text-stone-400"></i>
                  <span>수학 세특·탐구 주제</span>
                </button>
                <button type="button" onclick="selectTopic('이공계·대학 진로 상담')" data-topic="이공계·대학 진로 상담"
                  class="topic-chip p-3 rounded-xl border border-stone-200 hover:border-stone-300 bg-white text-stone-700 font-medium text-xs sm:text-sm flex items-center gap-2 transition text-left">
                  <i class="fa-solid fa-rocket text-base text-stone-400"></i>
                  <span>이공계·대학 진로 상담</span>
                </button>
                <button type="button" onclick="selectTopic('학교생활·교우관계·마음고민')" data-topic="학교생활·교우관계·마음고민"
                  class="topic-chip p-3 rounded-xl border border-stone-200 hover:border-stone-300 bg-white text-stone-700 font-medium text-xs sm:text-sm flex items-center gap-2 transition text-left">
                  <i class="fa-solid fa-heart text-base text-stone-400"></i>
                  <span>학교생활·마음 고민</span>
                </button>
                <button type="button" onclick="selectTopic('기타 자유 상담')" data-topic="기타 자유 상담"
