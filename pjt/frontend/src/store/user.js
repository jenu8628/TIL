import store from "../store";

const state = {
  user_id: "",
  user_email: "",
  user_info: 0
};

const getters = {
  getUserId: state => state.user_id,
  getUserEmail: state => state.user_email,
  getUserInfo: state => state.user_info
};

const mutations = {
  LOGIN_USER(state, user) {
    state.user_id = user["user_id"];
    state.user_email = user["user_email"];
    state.user_info = user["user_info"];
  },
  LOGOUT_USER(state) {
    state.user_id = "";
    state.user_email = "";
    state.user_email = "";
  }
};

const actions = {
  login_user(commit, user) {
    store.commit("LOGIN_USER", user);
  },
  logout_user() {
    store.commit("LOGOUT_USER");
  }
};

export default {
  state: {
    ...state
  },
  getters,
  mutations,
  actions
};
