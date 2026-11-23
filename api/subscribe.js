export default async function handler(req, res) {
  // Only accept POST requests
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { email, eventType } = req.body || {};
  if (!email) {
    return res.status(400).json({ error: 'Email is required' });
  }

  const RKSHAN_API_TOKEN = process.env.RKSHAN_API_TOKEN || "pops_h769dm9xngos_KhiiMLCTZBr_Pb6xJqdA_xifGLmQUvD6y5qGSOBeLHQ";
  const RKSHAN_HOST = "https://13-235-134-20.sslip.io";

  const payload = {
    schemaVersion: "1",
    sourceSystem: "shop",
    sourceEventId: "sub-" + Date.now() + "-" + Math.floor(Math.random() * 10000),
    eventType: eventType || "newsletter.subscribed",
    recipient: {
      externalRef: email,
      name: email.split('@')[0],
      email: email,
      language: "en"
    }
  };

  try {
    const rkshanRes = await fetch(`${RKSHAN_HOST}/api/v1/consent/requests`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${RKSHAN_API_TOKEN}`
      },
      body: JSON.stringify(payload)
    });

    const data = await rkshanRes.json().catch(() => ({}));
    return res.status(rkshanRes.status).json(data);
  } catch (error) {
    console.error("Rkshan automation error:", error);
    return res.status(500).json({ error: error.message || "Failed to contact Rkshan API" });
  }
}
