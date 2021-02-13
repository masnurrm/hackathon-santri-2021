import React, { useState } from 'react';
import { useForm } from 'react-hook-form';
import axios from 'axios';

export default function Pengaturan() {
	const { register, handleSubmit } = useForm();
	const [status, setStatus] = useState('');

	const submit = (data) => {
		if (data.password != data.repeat) {
			setStatus('Kata sandi tidak cocok!');
			return;
		} else {
			setStatus('');
		}

		setInterval(() => {
			setStatus('Kata sandi sudah berhasil diubah');
		}, 1000);
	};

	const sendPassword = () => {
		axios
			.post(`${process.env.REACT_APP_API_URL}/password_reset/`, {})
			.then((res) => {
				if (res.data.response) {
					setStatus('Link sudah dikirim ke email');
				} else {
					setStatus('Terjadi kesalahan');
				}
			})
			.catch((err) => {
				console.log(err);
				setStatus('Terjadi kesalahan');
			});
	};

	return (
		<form
			className="flex flex-col text-center	my-12 items-center max-w-4xl mx-auto"
			onSubmit={handleSubmit(submit)}
		>
			<span className="text-2xl my-2">Reset kata sandi</span>
			<span className="pt">Silahkan masukkan kata sandi baru</span>
			<span className="pt mt-4">{status}</span>

			<div className="form w-4/12 flex flex-col my-auto">
				<div class="flex my-2">
					<div class="input-icon">
						<i class="mdi mdi-key-outline text-gray-400 text-lg"></i>
					</div>
					<input
						type="password"
						name="password"
						ref={register}
						class="input-text"
						placeholder="Kata Sandi"
					/>
				</div>
				<div class="flex my-2">
					<div class="input-icon">
						<i class="mdi mdi-key-outline text-gray-400 text-lg"></i>
					</div>
					<input
						type="password"
						ref={register}
						name="repeat"
						class="input-text"
						placeholder="Ketik Ulang Kata Sandi"
					/>
				</div>

				<button className="gradient-button my-2" type="submit">
					KONFIRMASI
				</button>
			</div>
		</form>
	);
}
