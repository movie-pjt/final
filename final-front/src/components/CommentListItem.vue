<template>
  <div class="d-flex align-items-center mb-1 pb-1">
    <li class="comment-list-item mx-3 d-flex justify-content-between">
      <div class="d-flex align-items-center">
        <font-awesome-icon icon="fa-solid fa-user" />
        <!-- <router-link :to="{ name: 'profile', params: { username: comment.user.username } }">
          {{ comment.user.username }}
        </router-link> -->
        <div class="mx-1 me-3">
          {{ comment.user.username }}
        </div>
        <span v-if="!isEditing">{{ payload.content }}</span>
        <input v-if="isEditing" type="text" v-model="payload.content">

      </div>
      <div class="d-flex align-items-center">
        <div v-if="isEditing" class="d-flex align-items-center" style="margin-bottom: 2px;">
          <!-- <button @click="onUpdate">Update</button> |
          <button @click="switchIsEditing">Cancel</button> -->
          <font-awesome-icon icon="fa-solid fa-check"
          @click="onUpdate"
          class="fa-2x ed-btn"/>
          <font-awesome-icon icon="fa-solid fa-xmark"
          @click="switchIsEditing"
          class="fa-2x ed-btn"/>
        </div>
        <span v-if="currentUser.username === comment.user.username && !isEditing">
          <!-- <button @click="switchIsEditing"><font-awesome-icon icon="fa-solid fa-pen-to-square" /></button>
          <button @click="deleteComment(payload)">Delete</button> -->
          <font-awesome-icon icon="fa-solid fa-pen-to-square" 
          @click="switchIsEditing"
          class="fa-2x ed-btn"/>
          <font-awesome-icon icon="fa-solid fa-trash-can" 
          @click="deleteComment(payload)"
          class="fa-2x ed-btn"/>
        </span>
      </div>
    </li>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },

}
</script>

<style>
.comment-list-item {
  border-bottom: 1px solid white;
  width: 100%;
  font-size: 1.1rem;
}

.ed-btn {
  cursor: pointer;
	padding: 0px 0px 0px 20px;
	opacity: 0.5;
  width: 20px;
}

.ed-btn:hover {
	color: white;
	opacity: 1;
}
</style>