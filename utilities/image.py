
from bucket.bucket import BUCKET_NAME, get_bucket_client


class ImageUtil:
        
    def upload_images(self,product_sku_id: str, images: list) -> dict:

        image_dict = {}
        # Upload image to S3
        s3 = get_bucket_client()
        for i in range(len(images)):
            s3.upload_fileobj(images[i].file, BUCKET_NAME, f"{product_sku_id}/{i}.{images[i].filename.split('.')[-1]}")

            # Get image url
            image_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{product_sku_id}/{i}.jpg"

            image_dict[i] = image_url

        return image_dict


    def get_image_url(self):
        pass