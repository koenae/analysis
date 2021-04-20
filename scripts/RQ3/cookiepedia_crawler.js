const puppeteer = require('puppeteer');
const fs = require('fs');

(async => {
    getPurposesFromCookiepedia('france');
})();

async function getPurposesFromCookiepedia(country) {
    let cookie_names = require('../../cookie_names/' + country + '.json');

    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();

    const base_url = 'https://cookiepedia.co.uk/cookies/';

    let result = [];
    let counter = 0;
    for (let url of Object.keys(cookie_names)) {
        let cookie_purposes = [];
        let target_and_ad = 0;
        let necessary = 0;
        let functionality = 0;
        let performance = 0;
        let unknown = 0;
        console.log(url + ' - ' + counter++);
        for (let cookie_name of cookie_names[url]) {
            try {
                await page.goto(base_url + cookie_name);
                const description = await page.$eval('#content-left > p', el => el.textContent);
                const purpose = await page.$eval('#content-left > p > strong', el => el.textContent);
                cookie_purposes.push({
                    name: cookie_name,
                    description: description,
                    purpose: purpose
                });
                switch (purpose) {
                    case 'Targeting/Advertising':
                        target_and_ad++;
                        break;
                    case 'Strictly Necessary':
                        necessary++;
                        break;
                    case 'Functionality':
                        functionality++;
                        break;
                    case 'Performance':
                        performance++;
                        break;
                    case 'Unknown':
                        unknown++;
                        break;
                }
            } catch (error) {
                continue;
            }
        }
        result.push({
            url: url,
            cookies: cookie_purposes,
            target_and_ad: target_and_ad,
            necessary: necessary,
            functionality: functionality,
            performance: performance,
            unknown: unknown
        });
    }

    fs.writeFile('../../cookiepedia_purposes/' + country + '.json', JSON.stringify(result), function (err) {
        if (err) throw err;
        console.log('complete');
    }
    );

    await browser.close();
}