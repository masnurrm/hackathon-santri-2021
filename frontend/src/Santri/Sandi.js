import React, { useState } from 'react';
import axios from 'axios';

export default function Pengaturan() {
	const [nomor, setNomor] = useState();
	const [status, setStatus] = useState('');

	const submit = () => {
		let url = process.env.REACT_APP_API_URL;
		url = url.substr(0, url.length - 4);

		axios
			.post(`${url}/password_reset/`, {
				nomor_induk: nomor,
			})
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

	const handleNomor = (e) => setNomor(e.target.value);

	return (
		<div className="flex flex-col text-center	my-12 items-center max-w-4xl mx-auto">
			<span className="text-2xl my-2">Reset kata sandi</span>
			<span className="pt">
				Link untuk ubah kata sandi akan dikirim via email
			</span>
			<span
				className={`pt mt-4 ${
					status == 'Terjadi kesalahan' ? 'text-warn' : 'text-main'
				}`}
			>
				{status}
			</span>

			<div className="form w-4/12 flex flex-col my-auto">
				<div class="flex my-2">
					<div class="input-icon">
						<i class="mdi mdi-account-outline text-gray-400 text-lg"></i>
					</div>
					<input
						type="text"
						class="input-text"
						placeholder="Nomor Induk"
						onChange={(e) => handleNomor(e)}
					/>
				</div>

				<button className="gradient-button my-2" onClick={submit}>
					KONFIRMASI
				</button>
			</div>
		</div>
	);
}
