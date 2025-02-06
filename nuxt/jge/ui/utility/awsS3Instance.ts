import { S3Client } from '@aws-sdk/client-s3';
import { useRuntimeConfig } from 'nuxt/app';

let awsS3Instance: S3Client | null = null;

export function createAwsS3Instance() {
  if (!awsS3Instance) {
    const config = useRuntimeConfig();

    // config 값들을 string으로 명시적으로 캐스팅
    const region = config.public.AWS_REGION as string;
    const accessKeyId = config.public.AWS_ACCESS_KEY_ID as string;
    const secretAccessKey = config.public.AWS_SECRET_ACCESS_KEY as string;

    awsS3Instance = new S3Client({
      region,
      credentials: {
        accessKeyId,
        secretAccessKey,
      },
    });
  }

  return awsS3Instance;
}
