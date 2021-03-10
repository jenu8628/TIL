```vue
<template>
  <div>
    <div class="box1">
      <div>
        <h1
          class="box-above"
          id="h1-above"
          style="font-size: 3.5rem; opacity: 1; z-index: 1"
        >
          수만가지의 음식정보를 한번에
        </h1>
        <br>
        <h2
          class="box-above"
          id="h2-above"
          style="font-size: 2rem; opacity: 0.6; z-index: 1"
        >
          영양소 비교를 통한 식단관리를 도와드려요
        </h2>
        <img class="top-background" style="opacity: 0.9" :src="food" alt="" />
      </div>
    </div>
    <hr class="magin">
    <hr>
    <div class="box2">
      <img class="image-box" :src="food2" alt="" />
      <div>
        <h1 class="box-right" style="font-size: 3.5rem; opacity: 1; z-index: 1">
          당신의 음식을 기록하세요
        </h1>
        <hr>
        <h2
          class="box-right"
          style="font-size: 1.8rem; opacity: 0.6; z-index: 1"
        >
          섭취한 음식들을 통해 하루 권장 기준치와 영양소, 칼로리 등을 비교해
          드려요.
        </h2>
      </div>
    </div>
    <hr class="magin">
    <hr>
    <div class="box2">
      <div>
        <h1 class="box-left" style="font-size: 3.5rem; opacity: 1; z-index: 1">
          더이상 음식고민은 그만!
        </h1>
        <hr />
        <h2 class="box-left"
            style="font-size: 1.8rem; opacity: 0.6; z-index: 1">
          당신이 좋아하는 종류, 부족한 영양소, 적정 칼로리를 계산해서 음식을
          추천해 드려요.
        </h2>
      </div>
      <img class="image-box" :src="menu" alt="" />
    </div>
    <hr class="horizon">

    <div class="box2">
      <img class="image-box" :src="nutrient" alt="">
      <div>
        <h1 class="box-right" style="font-size: 3.5rem; opacity: 1; z-index: 1">
          영양소를 비교해드려요.
        </h1>
        <hr>
        <h2 class="box-right"
          style="font-size: 1.8rem; opacity: 0.6; z-index: 1">먹고 싶은 음식을 등록하세요. 음식 별 영양소를 비교해 드려요.</h2>
      </div>
    </div>
    <hr class="horizon">
    <div>
      <h1>식세끼 홍보 and 사용가이드</h1>
      <h3>사용가이드를 보고 다같이 건강한 식단관리를 시작해보아요.</h3>
    </div>
  </div>
</template>

<script>
import food from "../assets/img/main/food.png";
import food2 from "../assets/img/main/food2.jpg";
import menu from "../assets/img/main/menu.jpg";
import nutrient from "../assets/img/main/nutrient.jpg";

export default {
  data() {
    return {
      food: food,
      food2 : food2,
      menu: menu,
      nutrient : nutrient
    };
  },
  created() {
    window.addEventListener("scroll", this.onScroll);
  },
  destroyed() {
    window.removeEventListener("scroll", this.onScroll);
  },
  methods: {
    onScroll: function () {
      const vh = window.innerHeight;

      const img = document.querySelector("img");
      const h1 = document.querySelector("#h1-above");
      const h2 = document.querySelector("#h2-above");
      const bottom = document.querySelector("#bottom");

      let topImgVal = 0.9 + window.scrollY / -vh;
      let topTextVal1 = 1 + window.scrollY / -vh;
      let topTextVal2 = 0.6 + window.scrollY / -vh;
      let bottomVal = window.scrollY / vh - 0.3;

      img.style.opacity = topImgVal;
      h1.style.opacity = topTextVal1;
      h2.style.opacity = topTextVal2;
      bottom.style.opacity = bottomVal;
    },
  },
};
</script>

<style>
/* 이미지에 쓰인 클래스 */
.top-background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  pointer-events: none;
}
/* 제일 첫부분 큰 div에 넣는 클래스 */
.box1 {
  position: relative;
  max-width: 100%;
  height: 80vh;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  padding: 100px;
}
/* 첫부분 글자에 들어가는 클래스 */
.box-above {
  position: relative;
  color: aliceblue;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
/* 두번째부터 사용되는 제일 큰 클래스 */
.box2 {
  position: relative;
  max-width: 100%;
  height: 50vh;
  display: flex;
  justify-content: space-around;
  align-items: center;
  overflow: hidden;
  padding: 100px;
}
.box-right {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: flex-end;
  align-items: center;
}
.box-left {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
}
.image-box {
  position: relative;
  width: 30%;
  height: 80%;
  display: flex;
  justify-content: flex-start;
  align-items: center;
}
.horizon {
  position: relative;
  border-bottom: 8px solid rgb(141, 139, 139);
}
.magin {
  margin-bottom: 5px;
}
</style>
```

