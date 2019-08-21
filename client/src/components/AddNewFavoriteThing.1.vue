<template>
  <div>
    <b-modal
      v-bind:id="modalId"
      ref="modal"
      v-bind:title="modalTitle"
      @show="resetModal"
      @hidden="resetModal"
      @ok="handleOk"
    >
      <form ref="form" @submit.stop.prevent="handleSubmit">
        <b-form-group
          :state="titleState"
          label="Title"
          label-for="title-input"
          invalid-feedback="Title is required"
        >
          <b-form-input id="title-input" v-model="title" :state="titleState" required></b-form-input>
        </b-form-group>

        <b-form-group
          :state="rankState"
          label="Rank"
          label-for="rank-input"
          invalid-feedback="Rank is required"
        >
          <b-form-input id="rank-input" v-model="rank" :state="rankState" required type="number"></b-form-input>
        </b-form-group>

        <b-form-group label="Description" label-for="description-input">
          <b-form-input id="description-input" v-model="description"></b-form-input>
        </b-form-group>

        <b-form-group
          :state="categoryState"
          label="Category"
          label-for="category-input"
          invalid-feedback="Category is required"
        >
          <b-form-select
            id="category-input"
            v-model="category"
            :state="categoryState"
            required
            :options="getOptions"
            size="sm"
            class="mt-3"
          ></b-form-select>
        </b-form-group>

        <b-form-group label="metadata" label-for="metadata-input">
          <b-form-input id="metadata-input" v-model="metadata"></b-form-input>
        </b-form-group>
      </form>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AddNewCategory",
  props: ["modalId","modalTitle","categories", "title", "description","rank","category","metadata"],
  data() {
    return {
    //   title: this.title ? this.title : "",
    //   description: this.description ? this.description : "",
    //   rank: this.rank ? this.rank : "",
    //   category: this.category ? this.category : "",
    //   metadata: null,
      categoryState: null,
      titleState: null,
      rankState: null
    };
  },
  computed: {
    getOptions() {
      let options = [];
      this.categories.forEach(element => {
        let option = { value: element.id, text: element.name };
        options.push(option);
      });
      return options;
    }
  },
  methods: {
    checkFormValidity() {
      const valid = this.$refs.form.checkValidity();
      this.titleState = valid ? "valid" : "invalid";
      this.rankState = valid ? "valid" : "invalid";
      this.categoryState = valid ? "valid" : "invalid";
      return valid;
    },
    resetModal() {
      this.title = "";
      this.description = "";
      this.rank = "";
      this.category = "";
      this.metadata = null;
      this.titleState = null;
      this.categoryState = null;
      this.rankState = null;
    },
    handleOk(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      this.handleSubmit();
    },
    handleSubmit() {
      // Exit when the form isn't valid
      if (!this.checkFormValidity()) {
        return;
      }
      const newItem = {
        title: this.title,
        description: this.description,
        ranking: this.rank,
        category: this.category,
        metadata: this.metadata
      };
      this.$emit("addNewFavoriteThing", newItem);
      // Hide the modal manually
      this.$nextTick(() => {
        this.$refs.modal.hide();
      });
    }
  }
};
</script>
