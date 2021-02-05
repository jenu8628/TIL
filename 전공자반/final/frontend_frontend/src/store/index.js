import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";
import User from "./user";
import Token from "./token";
import Util from "./util";
import Kmap from "./kmap";
// import axios from "@/plugins/axios.js";

Vue.use(Vuex);

const store = new Vuex.Store({
  modules: {
    user: User,
    token: Token,
    util: Util,
    kmap: Kmap
  },
  plugins: [
    //주목! : 여기에 쓴 모듈만 저장됩니다.
    createPersistedState({
      paths: ["token", "user"]
    })
  ]
});

export default store;

// export default new Vuex.Store({
//   state: {
//     savePath: "",
//     accessToken: null,
//     user: {
//       userId: "",
//       userEmail: "",
//       userInfo: ""
//     }
//   },
//   getters: {
//     getSavePath(state) {
//       return state.savePath;
//     },
//     getAccessToken(state) {
//       return state.accessToken;
//     },
//     getUser(state) {
//       return state.user;
//     }
//   },
//   mutations: {
//     SAVEPATH(state, path) {
//       state.savePath = path;
//     },
//     LOGIN(state, payload) {
//       state.accessToken = payload["acc_token"];
//       let temp = payload["UserInfo"];
//       state.user.userId = temp["user_id"];
//       state.user.userEmail = temp["user_email"];
//       state.user.userInfo = temp["user_info"];
//     },
//     LOGOUT(state) {
//       state.accessToken = null;
//       state.userId = "";
//       state.userEmail = "";
//       state.userInfo = "";
//     }
//     // SETACCESSTOKEN(state, payload) {
//     //   state.accessToken = payload;
//     // },
//     // SETREFRESHTOKEN(state, payload) {
//     //   state.refreshToken = payload;
//     // },
//     // FINDTOKEN(state, payload) {
//     //   state.userId = payload["user-id"];
//     //   state.userEmail = payload["user-email"];
//     //   state.userInfo = payload["user-info"];
//     //   state.tokenState = true;
//     // }
//   },
//   actions: {
//     SAVEPATH(context, path) {
//       context.commit("SAVEPATH", path);
//     },
//     LOGIN(context, user) {
//       return axios.post(`/api/login`, user).then(response => {
//         if (response.status == 200) {
//           context.commit("LOGIN", response.data);
//           localStorage.setItem("acc_token", response.data["acc_token"]);
//           localStorage.setItem("ref_token", response.data["ref_token"]);
//           return true;
//         } else {
//           return false;
//         }
//       });
//     },
//     LOGOUT(context) {
//       context.commit("LOGOUT");
//       axios.defaults.headers.common["acc_token"] = "";
//       localStorage.removeItem("acc_token");
//       localStorage.removeItem("ref_token");
//       alert("로그아웃 완료");
//     }
//     // FINDTOKEN(context) {
//     //   let aToken = localStorage.getItem("AccessToken");
//     //   let rToken = localStorage.getItem("RefreshToken");
//     //   axios.defaults.headers.common["acc-token"] = aToken;
//     //   if (aToken && rToken) {
//     //     axios.get(`${SERVER_URL}/api/user/info`).then(aResponse => {
//     //       var aResult = aResponse.data["expire"];
//     //       if (aResult == "access") {
//     //         // Access Token 만료
//     //         axios.defaults.headers.common["acc-token"] = "";
//     //         axios.defaults.headers.common["ref-token"] = rToken;
//     //         axios
//     //           .get(`${SERVER_URL}/api/user/info`, {
//     //             headers: { "ref-token": rToken }
//     //           })
//     //           .then(rResponse => {
//     //             var rResult = rResponse.data["expire"];
//     //             if (rResult == "new") {
//     //               console.log("토큰 새로 발급");
//     //               aToken = rResponse.data["token"];
//     //               localStorage.setItem("AccessToken", aToken);
//     //               axios.defaults.headers.common["acc-token"] = aToken;
//     //               // 새로 발급받은 토큰으로 다시 정보 업로드
//     //               axios.get(`${SERVER_URL}/api/user/info`).then(response => {
//     //                 let temp = response.data["UserInfo"];
//     //                 temp.setItem("accessToken", aToken);
//     //                 temp.setItem("refreshToken", rToken);
//     //                 context.commit("LOGIN", temp);
//     //                 // context.commit("SETACCESSTOKEN", aToken);
//     //                 // context.commit("SETREFRESHTOKEN", rToken);
//     //               });
//     //             } else {
//     //               console.log("토큰 모두 만료");
//     //               localStorage.removeItem("AccessToken");
//     //               localStorage.removeItem("RefreshToken");
//     //             }
//     //           });
//     //       } else if (aResult == "no") {
//     //         // 문제있는 토큰
//     //         console.log("문제있는 토큰");
//     //         localStorage.removeItem("AccessToken");
//     //         localStorage.removeItem("RefreshToken");
//     //       } else {
//     //         // 살아있는 토큰
//     //         console.log("살아있는 토큰");
//     //         let temp = aResponse.data["UserInfo"];

//     //         // temp.setItem("accessToken", aToken);
//     //         // temp.setItem("refreshToken", rToken);
//     //         // context.commit("LOGIN", temp);
//     //         // context.commit("SETACCESSTOKEN", aToken);
//     //         // context.commit("SETREFRESHTOKEN", rToken);
//     //       }
//     //     });
//     //   } else {
//     //     console.log("토큰 비어있음");
//     //     localStorage.removeItem("AccessToken");
//     //     localStorage.removeItem("RefreshToken");
//     //   }
//     // }
//   },
//   methods: {},
//   modules: {}
// });
