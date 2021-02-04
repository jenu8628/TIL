<template>
  <div>
    <div align="right">
      <b-input-group class="mt-3 mb-3" style="width:350px">
        <b-form-input
          @keypress.enter="searchNotice"
          v-model="search"
        ></b-form-input>
        <b-input-group-append>
          <b-button @click="searchNotice" variant="primary">검색</b-button>
        </b-input-group-append>
      </b-input-group>
    </div>
    <table class="table table-hover">
      <thead style="text-align: center">
        <tr>
          <th style="width: 10%">글번호</th>
          <th style="width: 50%">글제목</th>
          <th style="width: 15%">작성자</th>
          <th style="width: 15%">작성시간</th>
          <th style="width: 10%">조회수</th>
        </tr>
      </thead>
      <tbody style="text-align: center">
        <tr v-for="notice in notices" :key="notice.notice_num">
          <td>{{ notice.notice_num }}</td>
          <td>
            <a @click="detail(notice.notice_num)"
              ><b>{{ notice.notice_title }}</b></a
            >
          </td>
          <td>{{ notice.notice_writer }}</td>
          <td>{{ notice.write_date }}</td>
          <td>{{ notice.notice_cnt }}</td>
        </tr>
        <tr>
          <td colspan="5"></td>
        </tr>
      </tbody>
    </table>
    <div>
      <ul class="pagination" style="justify-content: center; ">
        <li class="page-item" v-if="startPage > 1">
          <a class="page-link" @click="frontPage">이전</a>
        </li>
        <div v-for="i in endPage" :key="i">
          <li class="page-item active" v-if="i == curPage">
            <a class="page-link" v-if="i >= startPage">{{ i }}</a>
          </li>
          <li class="page-item" v-if="i != curPage">
            <a class="page-link" v-if="i >= startPage" @click="selPage(i)">{{
              i
            }}</a>
          </li>
        </div>
        <li class="page-item" v-if="endPage < totalPage">
          <a class="page-link" @click="backPage">다음</a>
        </li>
      </ul>
    </div>
    <div>
      <button
        class="btn btn-primary"
        @click="regist"
        v-if="this.$store.getters.getUserInfo == 1"
      >
        글쓰기
      </button>
    </div>
  </div>
</template>

<script>
import axios from "@/plugins/axios";
export default {
  created() {
    axios
      .get(
        "/api/notice/list?name=" +
          this.$store.getters.getSearchTitle +
          "&page=" +
          this.$store.getters.getSearchPage
      )
      .then(response => {
        this.notices = response.data["list"];
        this.curPage = response.data["curPage"];
        this.startPage = response.data["startPage"];
        this.endPage = response.data["endPage"];
        this.totalPage = response.data["totalPage"];
      });
  },
  data() {
    return {
      notices: [],
      curPage: 1,
      startPage: 0,
      endPage: 0,
      totalPage: 0,
      search: ""
    };
  },
  methods: {
    selPage(page) {
      axios
        .get("/api/notice/list?name=" + this.search + "&page=" + page)
        .then(response => {
          this.notices = response.data["list"];
          this.curPage = response.data["curPage"];
          this.startPage = response.data["startPage"];
          this.endPage = response.data["endPage"];
          this.totalPage = response.data["totalPage"];
        });
    },
    frontPage() {
      axios
        .get(
          "/api/notice/list?name=" +
            this.search +
            "&page=" +
            (this.startPage - 1)
        )
        .then(response => {
          this.notices = response.data["list"];
          this.curPage = response.data["curPage"];
          this.startPage = response.data["startPage"];
          this.endPage = response.data["endPage"];
          this.totalPage = response.data["totalPage"];
        })
        .catch(error => {
          console.log(error);
        });
    },
    backPage() {
      axios
        .get(
          "/api/notice/list?name=" + this.search + "&page=" + (this.endPage + 1)
        )
        .then(response => {
          this.notices = response.data["list"];
          this.curPage = response.data["curPage"];
          this.startPage = response.data["startPage"];
          this.endPage = response.data["endPage"];
          this.totalPage = response.data["totalPage"];
        })
        .catch(error => {
          console.log(error);
        });
    },
    regist() {
      this.$router.push("/notice/regist");
    },
    detail(num) {
      this.$store.dispatch("update_searchdata", {
        search: this.search,
        page: this.curPage
      });
      this.$router.push("/notice/" + num);
    },
    searchNotice() {
      this.$store.dispatch("update_searchdata", {
        search: this.search,
        page: this.curPage
      });
      axios
        .get("/api/notice/list?name=" + this.search + "&page=1")
        .then(response => {
          this.notices = response.data["list"];
          this.curPage = response.data["curPage"];
          this.startPage = response.data["startPage"];
          this.endPage = response.data["endPage"];
          this.totalPage = response.data["totalPage"];
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style></style>
