import React from 'react';

export default function Pengaturan() {
	return (
		<div className="flex flex-col text-center	my-12 items-center max-w-4xl mx-auto">
			<span className="text-2xl my-2">Detail Laporan</span>
			<span className="pt mb-6">Pengaturan ubah kata sandi </span>

			<div className="form w-4/12 flex flex-col my-auto">
				<div class="flex my-2">
					<div class="input-icon">
						<i class="mdi mdi-account-outline text-gray-400 text-lg"></i>
					</div>
					<input type="text" class="input-text" placeholder="Nomor Induk" />
				</div>

				<div class="flex my-2">
					<div class="input-icon">
						<i class="mdi mdi-key-outline text-gray-400 text-lg"></i>
					</div>
					<input
						type="password"
						class="input-text"
						placeholder="Kata Sandi Lama"
					/>
				</div>

				<div class="flex my-2">
					<div class="input-icon">
						<i class="mdi mdi-key-outline text-gray-400 text-lg"></i>
					</div>
					<input
						type="password"
						class="input-text"
						placeholder="Kata Sandi Baru"
					/>
				</div>

				<button className="gradient-button my-2">KONFIRMASI</button>
			</div>
		</div>
	);
}
