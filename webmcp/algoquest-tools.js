const base = new URL("./", document.baseURI);

async function loadJson(path) {
  const response = await fetch(new URL(path, base));
  if (!response.ok) throw new Error(`Unable to load ${path}: ${response.status}`);
  return response.json();
}

function registerReadOnlyTool(name, description, inputSchema, execute) {
  const context = document.modelContext;
  if (!context?.registerTool) return false;
  context.registerTool({name, description, inputSchema, annotations: {readOnlyHint: true}}, execute);
  return true;
}

registerReadOnlyTool("algoquest_list_packets", "List production prompt packets and readiness.", {type: "object", properties: {}}, async () => loadJson("agent/packets.json"));
registerReadOnlyTool("algoquest_list_books", "List the six canonical AlgoQuest books and production scope.", {type: "object", properties: {}}, async () => loadJson("agent/books.json"));
registerReadOnlyTool("algoquest_get_prompt_packet", "Get one resolved or blocked prompt packet by ID.", {type: "object", required: ["packet_id"], properties: {packet_id: {type: "string"}}}, async ({packet_id}) => {
  const data = await loadJson("agent/packet-details.json");
  const packet = data.packets[packet_id.toUpperCase()];
  if (!packet) throw new Error(`Unknown packet: ${packet_id}`);
  return packet;
});
registerReadOnlyTool("algoquest_get_jobs", "Read production jobs and dependencies.", {type: "object", properties: {}}, async () => loadJson("agent/jobs.json"));
registerReadOnlyTool("algoquest_get_job_dependencies", "Get one production job and the states of its direct dependencies.", {type: "object", required: ["job_id"], properties: {job_id: {type: "string"}}}, async ({job_id}) => {
  const data = await loadJson("agent/jobs.json");
  const job = data.jobs.find(item => item.job_id === job_id);
  if (!job) throw new Error(`Unknown job: ${job_id}`);
  return {job, dependencies: job.depends_on.map(id => data.jobs.find(item => item.job_id === id))};
});
registerReadOnlyTool("algoquest_get_image_slots", "Read the complete image slot registry.", {type: "object", properties: {}}, async () => loadJson("agent/image-slots.json"));
registerReadOnlyTool("algoquest_search_sources", "Search source IDs, URLs, topics and coverage.", {type: "object", required: ["query"], properties: {query: {type: "string", minLength: 1}}}, async ({query}) => {
  const response = await fetch(new URL("agent/research-sources.jsonl", base));
  if (!response.ok) throw new Error(`Unable to load sources: ${response.status}`);
  const needle = query.toLocaleLowerCase();
  return (await response.text()).trim().split("\n").map(JSON.parse).filter(item => JSON.stringify(item).toLocaleLowerCase().includes(needle)).slice(0, 50);
});
