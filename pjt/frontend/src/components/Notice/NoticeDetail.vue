<template>
  <div>
    <table class="table table-hover" style="margin-top:70px">
      <thead>
        <tr>
          <th colspan="4">
            <h4 style="margin-top:10px; margin-bottom:10px">
              {{ detail.notice_title }}
            </h4>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td width="70%"></td>
          <td style="text-align:right" width="10%">
            <b>{{ detail.notice_writer }}</b>
          </td>
          <td style="text-align:right" width="10%">
            조회수 {{ detail.notice_cnt }}
          </td>
          <td style="text-align:right" width="10%">{{ detail.write_date }}</td>
        </tr>
      </tbody>
    </table>
    <div>
      <h5 style="margin-top:60px; margin-bottom:200px">
        {{ detail.notice_content }}
      </h5>
    </div>
    <div v-if="this.$store.getters.getUserInfo == 1">
      <button @click="delNotice" class="btn btn-primary mb-5 mr-2">
        귿삭제
      </button>
      <button @click="modifyNotice" class="btn btn-primary mb-5 ml-2">
        글수정
      </button>
    </div>
  </div>
</template>

<script>
import axios from "@/plugins/axios";
export default {
  created() {
    axios.get("/api/notice/" + this.$route.params.nno).then(response => {
      this.detail = response.data;
    });
  },
  data() {
    return {
      detail: {}
    };
  },
  methods: {
    delNotice() {
      axios.delete("/api/notice/" + this.$route.params.nno).then(response => {
        if (response.status == 200) {
          alert("공지사항 삭제 완료");
          this.$router.push("/notice");
        } else {
          alert("공지사항 삭제 실패");
        }
      });
    },
    modifyNotice() {
      this.$router.push("/notice/" + this.$route.params.nno + "/modify");
    }
  }
};
</script>

<style></style>
