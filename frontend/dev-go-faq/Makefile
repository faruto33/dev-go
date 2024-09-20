docker_build :
	docker build -t  ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GCP_REPO_NAME}/${GAR_IMAGE}:dev .

docker_push :
	docker push ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GCP_REPO_NAME}/${GAR_IMAGE}:dev

gcloud_run :
	gcloud run deploy --image ${GCP_REGION}-docker.pkg.dev/${GCP_PROJECT}/${GCP_REPO_NAME}/${GAR_IMAGE}:dev --memory ${GAR_MEMORY} --region ${GCP_REGION}
