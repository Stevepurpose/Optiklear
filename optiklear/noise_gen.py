import random
import numpy as np
import copy


def unif_noise(image, lower, upper):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            noise = random.uniform(lower, upper)
            noisy_pixel = image[i, j] + noise
            noisy_pixel = np.clip(noisy_pixel, 0, 255)
            image[i, j] = np.uint8(np.round(noisy_pixel))
            
    return image



def gauss_noise(image, std):
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            noise = random.gauss(mu=0.0, sigma=std)
            noisy_pixel = image[i, j] + noise
            noisy_pixel = np.clip(noisy_pixel, 0, 255)
            image[i, j] = np.uint8(np.round(noisy_pixel))
    return image




def salt_pepper_noise(image, prob_pepper, prob_salt):

    copied_image = copy.deepcopy(image)

    for i in range(len(copied_image)):
        for j in range(len(copied_image[i])):

            rand_num = random.random()

            if rand_num < prob_pepper:
                copied_image[i][j] = 0

            elif rand_num > 1 - prob_salt:
                copied_image[i][j] = 255

    return copied_image