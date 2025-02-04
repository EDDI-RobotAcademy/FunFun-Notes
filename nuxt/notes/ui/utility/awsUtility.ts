import { useRuntimeConfig } from 'nuxt/app';

export const getS3ImageUrl = (imagePath: string) => {
  const config = useRuntimeConfig();
  const s3BucketName = config.public.AWS_BUCKET_NAME; // S3 버킷 이름
  const s3Region = config.public.AWS_REGION; // S3 버킷의 리전
  
  return `https://${s3BucketName}.s3.${s3Region}.amazonaws.com/${imagePath}`; // 완전한 S3 URL 반환
};
