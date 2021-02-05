import Vue from "vue";
import VueRouter from "vue-router";
import Login from "../views/Login.vue";

import Home from "@/views/Home.vue";
import Me from "@/views/Me.vue";
import Signup from "@/views/Signup.vue";

import Notice from "@/views/Notice.vue";
import NoticeList from "@/components/Notice/NoticeTable.vue";
import NoticeRegist from "@/components/Notice/NoticeRegist.vue";
import NoticeDetail from "@/components/Notice/NoticeDetail.vue";
import NoticeModify from "@/components/Notice/NoticeModify.vue";

import Board from "@/views/Board.vue";
import BoardTable from "@/components/Board/BoardTable.vue";
import BoardRegist from "@/components/Board/BoardRegist.vue";
import BoardDetail from "@/components/Board/BoardDetail.vue";
import BoardModify from "@/components/Board/BoardModify.vue";

import store from "../store/index";

Vue.use(VueRouter);

const requireAuth = () => async (to, from, next) => {
  // 토큰이 있는 경우
  let token = store.getters.getAccToken;
  if (token != null && token.length > 0) {
    return next();
  }
  // 경로 미리 저장
  const nextRoute = to.path;
  console.log(nextRoute);
  store.dispatch("update_savepath", nextRoute);
  // 토큰이 없으면 진입 불가
  alert("로그인 후 이용가능합니다.");
  return next("/login");
};

const logoutCheck = () => async (to, from, next) => {
  let token = store.getters.getAccToken;
  if (token == null || token.length == 0) {
    return next();
  }
  return next("");
};

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/login",
    name: "Loign",
    component: Login
  },
  {
    path: "/me",
    name: "Me",
    component: Me,
    beforeEnter: requireAuth()
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
    beforeEnter: logoutCheck()
  },
  {
    path: "/notice",
    // name: "Notice",
    component: Notice,
    children: [
      { path: "", name: "NoticeList", component: NoticeList },
      { path: "regist", name: "NoticeRegist", component: NoticeRegist },
      { path: ":nno", name: "NoticeDetail", component: NoticeDetail },
      { path: ":nno/modify", name: "NoticeModify", component: NoticeModify }
    ]
  },
  {
    path: "/board",
    // name: "Board",
    component: Board,
    children: [
      { path: "", name: "BoardTable", component: BoardTable },
      { path: "regist", name: "BoardRegist", component: BoardRegist },
      { path: ":bno", name: "BoardDetail", component: BoardDetail },
      { path: ":nno/modify", name: "BoardModify", component: BoardModify }
    ]
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
