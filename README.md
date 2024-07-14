# WalletChecker

Have you ever seen those wallet checker apps that, when installed, check a lot of 12-word seeds with a connected wallet and tell you if it has some funds or is empty? There are a lot of them, even here on GitHub. 

Literally, all of them operate like this: 

1. You install their app. No virus (mostly). Everything looks good.
2. You start checking random seeds.
3. After some time, you see a seed's wallet with some funds.
4. You can't see the full seed, so you can't access those funds.
5. You need to "buy" the app at an extreme price to unlock the "full seed" feature.
6. You pay because you found a $1,000 BTC wallet, and you just need to pay $200 first.
   
    **7-1:** 
    - You get the seed.
    - You see there is literally nothing in that wallet.
    - Congrats, you got scammed.
    
    **7-2:**
    - You don't get anything at all. The app stops working or does not find any wallets.
    - You got scammed again.

If you want to see some of these apps, just search "bitcoin hacking" tag on GitHub. Even if you see the source codes of those apps, they will never work. Either the source codes are incomplete, or it’s just random stuff to prove their app is legit. I'm sure the only near-working (in theory) wallet checker is going to be something like mine here.

### Related

1. I haven't paid anything for such apps. I just researched like any other normal human would if they saw something this unbelievable.
2. To prove it's not possible to get a wallet with funds when randomly checking everything, I kept the code running for about 5 days, and it checked 50,000,000 wallets.
3. There are 2048 unique seed words, so the total amount of possible bitcoin wallets is 2048¹², which is 5,444,517,870,735,015,415,413,993,718,908,291,383,296 in total. The chance of you finding one with funds is the same as you reading this whole number correctly on the first try.
4. Now don't be sad knowing you can't wake up to $100,000 in a wallet you stole. You may get something far better than cash in your life: knowledge.
5. It's not a good idea to keep running the code for a long time because it's essentially spam-checking wallets no one even uses. You may just experiment with crypto stuff.
