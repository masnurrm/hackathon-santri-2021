import React from 'react';

export default function Pengaduan() {
	return (
		<div className="flex flex-col text-center	my-12 items-center max-w-4xl mx-auto">
			<span className="text-2xl my-2">Pengaduan</span>
			<span className="pt mb-6">
				Kolom pengaduan layanan atau lupa kata sandi
			</span>

			<div className="form w-4/12 flex flex-col my-auto">
				<div class="flex my-2">
					<div class="input-icon">
						<i class="mdi mdi-account-outline text-gray-400 text-lg"></i>
					</div>
					<input type="text" class="input-text" placeholder="Nomor Identitas" />
				</div>

				<div class="flex my-2">
					<div class="input-icon">
						<i class="mdi mdi-key-outline text-gray-400 text-lg"></i>
					</div>
					<input type="text" class="input-text" placeholder="Email" />
				</div>

				<div class="flex my-2">
					<div class="input-icon self-start my-2">
						<i class="mdi mdi-email-outline text-gray-400 text-lg"></i>
					</div>
					<textarea class="input-text" placeholder="Pesan" height="10" />
				</div>

				<button className="gradient-button my-2">KIRIM</button>
			</div>
		</div>
	);
}
