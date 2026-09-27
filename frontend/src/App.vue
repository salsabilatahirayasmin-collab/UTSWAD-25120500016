<template>
  <div class="container">
    <h1>Pemesanan Shuttle Kampus</h1>

    <!-- Form Create -->
    <div class="form-card">
      <h2>Tambah Sesi</h2>
      <form @submit.prevent="createSession">
        <input v-model="form.rute" placeholder="Rute (misal: Gedung A - Gedung B)" />
        <p v-if="errors.rute" class="error">{{ errors.rute }}</p>
        
        <input v-model="form.waktu" placeholder="Waktu (misal: 08:00)" />
        <p v-if="errors.waktu" class="error">{{ errors.waktu }}</p>
        
        <input v-model.number="form.kapasitas" type="number" placeholder="Kapasitas" />
        <p v-if="errors.kapasitas" class="error">{{ errors.kapasitas }}</p>
        
        <button type="submit" :disabled="submitting">Simpan</button>
      </form>
    </div>

    <!-- State: Loading -->
    <div v-if="loading">Memuat data...</div>

    <!-- State: Error + Retry -->
    <div v-else-if="error" class="error-box">
      <p>{{ error }}</p>
      <button @click="fetchSessions">Coba Lagi (Retry)</button>
    </div>

    <!-- State: Empty -->
    <div v-else-if="sessions.length === 0">
      <p>Tidak ada data sesi.</p>
    </div>

    <!-- State: Success -->
    <table v-else>
      <thead>
        <tr><th>ID</th><th>Rute</th><th>Waktu</th><th>Kapasitas</th><th>Terisi</th><th>Aksi</th></tr>
      </thead>
      <tbody>
        <tr v-for="s in sessions" :key="s.id">
          <td>{{ s.id }}</td>
          <td>{{ s.rute }}</td>
          <td>{{ s.waktu }}</td>
          <td>{{ s.kapasitas }}</td>
          <td>{{ s.terisi }}</td>
          <td><button @click="confirmDelete(s.id)">Hapus</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const API_URL = 'http://localhost:8000/sessions';

const sessions = ref([]);
const loading = ref(false);
const error = ref(null);
const submitting = ref(false);
const errors = ref({});

const form = ref({ rute: '', waktu: '', kapasitas: 1 });

const fetchSessions = async () => {
  loading.value = true;
  error.value = null;
  try {
    const res = await axios.get(API_URL);
    sessions.value = res.data.data;
  } catch (err) {
    error.value = 'Gagal memuat data. Silakan coba lagi.';
  } finally {
    loading.value = false;
  }
};

const validateForm = () => {
  errors.value = {};
  if (!form.value.rute) errors.value.rute = 'Rute harus diisi.';
  if (!form.value.waktu) errors.value.waktu = 'Waktu harus diisi.';
  if (form.value.kapasitas <= 0) errors.value.kapasitas = 'Kapasitas harus > 0.';
  return Object.keys(errors.value).length === 0;
};

const createSession = async () => {
  if (!validateForm()) return;
  submitting.value = true;
  try {
    await axios.post(API_URL, form.value);
    form.value = { rute: '', waktu: '', kapasitas: 1 };
    await fetchSessions();
  } catch (err) {
    error.value = 'Gagal menambah data.';
  } finally {
    submitting.value = false;
  }
};

const confirmDelete = async (id) => {
  if (!confirm('Apakah Anda yakin ingin menghapus sesi ini?')) return;
  try {
    await axios.delete(`${API_URL}/${id}`);
    await fetchSessions();
  } catch (err) {
    error.value = 'Gagal menghapus data.';
  }
};

onMounted(fetchSessions);
</script>

<style scoped>
.container { max-width: 800px; margin: auto; padding: 1rem; font-family: sans-serif; }
.form-card { border: 1px solid #ccc; padding: 1rem; margin-bottom: 1rem; background: #f9f9f9; }
input { display: block; width: 100%; margin-bottom: 0.5rem; padding: 0.5rem; }
.error { color: red; font-size: 0.8rem; margin-top: -0.4rem; margin-bottom: 0.5rem; }
.error-box { color: red; border: 1px solid red; padding: 1rem; background: #ffe6e6; }
table { width: 100%; border-collapse: collapse; margin-top: 1rem; }
th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
th { background-color: #f2f2f2; }
button { cursor: pointer; padding: 0.4rem 0.8rem; }
</style>